"""A more liberal autolinker

Inspired by Django's urlize function.

Positive examples:
"""

import markdown
import urllib
import os
from hashlib import sha1
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
