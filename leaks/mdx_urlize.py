"""A more liberal autolinker

Inspired by Django's urlize function.

Positive examples:

>>> import markdown
>>> md = markdown.Markdown(extensions=['urlize'])

>>> md.convert('http://example.com/')
u'<p><a href="http://example.com/">http://example.com/</a></p>'

>>> md.convert('go to http://example.com')
u'<p>go to <a href="http://example.com">http://example.com</a></p>'

>>> md.convert('example.com')
u'<p><a href="http://example.com">example.com</a></p>'

>>> md.convert('example.net')
u'<p><a href="http://example.net">example.net</a></p>'

>>> md.convert('www.example.us')
u'<p><a href="http://www.example.us">www.example.us</a></p>'

>>> md.convert('(www.example.us/path/?name=val)')
u'<p>(<a href="http://www.example.us/path/?name=val">www.example.us/path/?name=val</a>)</p>'

>>> md.convert('go to <http://example.com> now!')
u'<p>go to <a href="http://example.com">http://example.com</a> now!</p>'

>>> md.convert('http://example.com/abc.png')
u'<img src="http://example.com/abc.png" />'

Negative examples:

>>> md.convert('del.icio.us')
u'<p>del.icio.us</p>'

"""

import markdown
import urllib
import os
from io import StringIO
from hashlib import sha1
from PIL import Image
from django.conf import settings

from markdown.util import etree, AtomicString
from mimetypes import guess_type, guess_extension

# Global Vars
URLIZE_RE = '(%s)' % '|'.join([
    r'<(?:f|ht)tps?://[^>]*>',
    r'\b(?:f|ht)tps?://[^)<>\s]+[^.,)<>\s]',
    r'\bwww\.[^)<>\s]+[^.,)<>\s]',
    r'[^(<\s]+\.(?:com|net|org)\b',
])

def process_image(image_url):
    file_type = guess_type(image_url)
    ext = file_type[0].split('/')[1]
    image_name = '.'.join((sha1(image_url).hexdigest()[:6], ext))
    image_path = os.path.join(settings.UPLOAD_DIR, image_name)

    if not os.path.exists(image_path):
        from ipdb import set_trace; set_trace()
        urllib.urlretrieve(image_url, image_path)
            
    return '/'.join((settings.UPLOAD_URL, image_name))

class UrlizePattern(markdown.inlinepatterns.Pattern):
    """ Return a link Element given an autolink (`http://example/com`). """
    def handleMatch(self, m):
        url = m.group(2)
        
        if url.startswith('<'):
            url = url[1:-1]
            
        text = url
        
        if not url.split('://')[0] in ('http','https','ftp'):
            if '@' in url and not '/' in url:
                url = 'mailto:' + url
            else:
                url = 'http://' + url
        mime_type = guess_type(url)
        if mime_type[0] and 'image' in mime_type[0]:
            el = etree.Element("img")
            el.set('src', process_image(url))
        else:
            el = etree.Element("a")
            el.set('href', url)
            el.text = AtomicString(text)
        return el

class UrlizeExtension(markdown.Extension):
    """ Urlize Extension for Python-Markdown. """

    def extendMarkdown(self, md, md_globals):
        """ Replace autolink with UrlizePattern """
        md.registerExtension(self)
        md.inlinePatterns['urlize'] = UrlizePattern(URLIZE_RE, md)

def makeExtension(configs=None):
    if configs is None: configs = {}
    return UrlizeExtension(configs=configs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
