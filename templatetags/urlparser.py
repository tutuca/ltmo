import re
import string

from django import template
from django.utils.functional import allow_lazy
from django.utils.safestring import SafeData, mark_safe, mark_for_escaping
from django.utils.encoding import force_unicode
from django.template.defaultfilters import stringfilter
from django.utils.http import urlquote

register = template.Library()

# Configuration for imgfromurl() function.
LEADING_PUNCTUATION  = ['(', '<', '&lt;']
TRAILING_PUNCTUATION = ['.', ',', ')', '>', '\n', '&gt;']

word_split_re = re.compile(r'(\s+)')
punctuation_re = re.compile('^(?P<lead>(?:%s)*)(?P<middle>.*?)(?P<trail>(?:%s)*)$' % \
    ('|'.join([re.escape(x) for x in LEADING_PUNCTUATION]),
    '|'.join([re.escape(x) for x in TRAILING_PUNCTUATION])))


def image_from_url(text):
    """
    Reworked from django's urlize.
    
    Tries to get an image from a link if the extension is one of jpg, png, gif
    """
    safe_input = isinstance(text, SafeData)
    words = word_split_re.split(force_unicode(text))
    for i, word in enumerate(words):
        match = None
        if '.' in word or ':' in word:
            match = punctuation_re.match(word)
        if match:
            lead, middle, trail = match.groups()

            # Make URL we want to point to.
            url = None
            if middle.startswith('http://') or middle.startswith('https://'):
                url = urlquote(middle, safe='/&=:;#?+*')
            elif middle.startswith('www.') or ('@' not in middle and \
                    middle and middle[0] in string.ascii_letters + string.digits and \
                    (middle.endswith('.org') or middle.endswith('.net') or middle.endswith('.com'))):
                url = urlquote('http://%s' % middle, safe='/&=:;#?+*')

            # Make link.
            if url and url[-3:] in ('jpg', 'jpeg', 'png', 'gif', 'JPEG' , 'JPG','PNG','GIF' ):
                if not safe_input:
                    lead, trail = mark_for_escaping(lead), mark_for_escaping(trail)
                    url = mark_for_escaping(url)

                middle = '<img src="%s" />' % (url)
                words[i] = mark_safe('%s%s%s' % (lead, middle, trail))
            else:
                if safe_input:
                    words[i] = mark_safe(word)
                    words[i] = mark_for_escaping(word)
        elif safe_input:
            words[i] = mark_safe(word)
    return u''.join(words)

image_from_url = allow_lazy(image_from_url, unicode)

@register.filter
@stringfilter
def url_to_img(value):
    """Converts URLs in plain text into clickable links."""
    return mark_safe(image_from_url(value))
    
image_from_url.is_safe=True
