#!/usr/bin/env python

"""
Embeds web videos using URLs.  For instance, if a URL to an youtube video is
found in the text submitted to markdown and it isn't enclosed in parenthesis
like a normal link in markdown, then the URL will be swapped with a embedded
youtube video.

All resulting HTML is XHTML Strict compatible.
"""

import markdown
from markdown.util import etree

version = "0.1.6"

class VideoExtension(markdown.Extension):
    def __init__(self, configs):
        self.config = {
            'bliptv_width': ['480', 'Width for Blip.tv videos'],
            'bliptv_height': ['300', 'Height for Blip.tv videos'],
            'dailymotion_width': ['480', 'Width for Dailymotion videos'],
            'dailymotion_height': ['405', 'Height for Dailymotion videos'],
            'gametrailers_width': ['480', 'Width for Gametrailers videos'],
            'gametrailers_height': ['392', 'Height for Gametrailers videos'],
            'metacafe_width': ['498', 'Width for Metacafe videos'],
            'metacafe_height': ['423', 'Height for Metacafe videos'],
            'veoh_width': ['410', 'Width for Veoh videos'],
            'veoh_height': ['341', 'Height for Veoh videos'],
            'vimeo_width': ['400', 'Width for Vimeo videos'],
            'vimeo_height': ['321', 'Height for Vimeo videos'],
            'yahoo_width': ['512', 'Width for Yahoo! videos'],
            'yahoo_height': ['322', 'Height for Yahoo! videos'],
            'youtube_width': ['425', 'Width for Youtube videos'],
            'youtube_height': ['344', 'Height for Youtube videos'],
        }

        # Override defaults with user settings
        for key, value in configs:
            self.setConfig(key, value)

    def add_inline(self, md, name, klass, re):
        pattern = klass(re)
        pattern.md = md
        pattern.ext = self
        md.inlinePatterns.add(name, pattern, "<reference")

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        self.add_inline(md, 'bliptv', Bliptv,
            r'([^(]|^)http://(\w+\.|)blip.tv/file/get/(?P<bliptvfile>\S+.flv)')
        self.add_inline(md, 'dailymotion', Dailymotion,
            r'([^(]|^)http://www\.dailymotion\.com/(?P<dailymotionid>\S+)')
        self.add_inline(md, 'gametrailers', Gametrailers,
            r'([^(]|^)http://www.gametrailers.com/video/[a-z0-9-]+/(?P<gametrailersid>\d+)')
        self.add_inline(md, 'metacafe', Metacafe,
            r'([^(]|^)http://www\.metacafe\.com/watch/(?P<metacafeid>\S+)/')
        self.add_inline(md, 'veoh', Veoh,
            r'([^(]|^)http://www\.veoh\.com/\S*(#watch%3D|watch/)(?P<veohid>\w+)')
        self.add_inline(md, 'vimeo', Vimeo,
            r'([^(]|^)http://(www.|)vimeo\.com/(?P<vimeoid>\d+)\S*')
        self.add_inline(md, 'yahoo', Yahoo,
            r'([^(]|^)http://video\.yahoo\.com/watch/(?P<yahoovid>\d+)/(?P<yahooid>\d+)')
        # http://www.youtube.com/watch?v=R2fwHjLvvk4&feature=rec-LGOUT-exp_stronger_r2-2r-1-HM
        # http://www.youtube.com/v/0Xfh5iBBh4Y?fs=1&hl=en_US
        self.add_inline(md, 'youtube', Youtube,
            r'([^("\']|^)http://www\.youtube\.com/(?:watch\?\S*v=|v\/)(?P<youtubeargs>[A-Za-z0-9_&=-]+)\S*')

class Bliptv(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/file/get/%s' % m.group('bliptvfile')
        width = self.ext.config['bliptv_width'][0]
        height = self.ext.config['bliptv_height'][0]
        return flash_object(url, width, height)

class Dailymotion(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.dailymotion.com/swf/%s' % m.group('dailymotionid').split('/')[-1]
        width = self.ext.config['dailymotion_width'][0]
        height = self.ext.config['dailymotion_height'][0]
        return flash_object(url, width, height)

class Gametrailers(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.gametrailers.com/remote_wrap.php?mid=%s' % \
            m.group('gametrailersid').split('/')[-1]
        width = self.ext.config['gametrailers_width'][0]
        height = self.ext.config['gametrailers_height'][0]
        return flash_object(url, width, height)

class Metacafe(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.metacafe.com/fplayer/%s.swf' % m.group('metacafeid')
        width = self.ext.config['metacafe_width'][0]
        height = self.ext.config['metacafe_height'][0]
        return flash_object(url, width, height)

class Veoh(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.veoh.com/videodetails2.swf?permalinkId=%s' % m.group('veohid')
        width = self.ext.config['veoh_width'][0]
        height = self.ext.config['veoh_height'][0]
        return flash_object(url, width, height)

class Vimeo(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://vimeo.com/moogaloop.swf?clip_id=%s&amp;server=vimeo.com' % m.group('vimeoid')
        width = self.ext.config['vimeo_width'][0]
        height = self.ext.config['vimeo_height'][0]
        return flash_object(url, width, height)

class Yahoo(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = "http://d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf?ver=2.2.40"
        width = self.ext.config['yahoo_width'][0]
        height = self.ext.config['yahoo_height'][0]
        obj = flash_object(url, width, height)
        param = etree.Element('param')
        param.set('name', 'flashVars')
        param.set('value', "id=%s&vid=%s" % (m.group('yahooid'),
                m.group('yahoovid')))
        obj.append(param)
        return obj

class Youtube(markdown.inlinepatterns.Pattern):
    def handleMatch(self, m):
        url = 'http://www.youtube.com/v/%s' % m.group('youtubeargs')
        width = self.ext.config['youtube_width'][0]
        height = self.ext.config['youtube_height'][0]
        return flash_object(url, width, height)

def flash_object(url, width, height):
        obj = etree.Element('object')
        obj.set('type', 'application/x-shockwave-flash')
        obj.set('width', width)
        obj.set('height', height)
        obj.set('data', url)
        param = etree.Element('param')
        param.set('name', 'movie')
        param.set('value', url)
        obj.append(param)
        param = etree.Element('param')
        param.set('name', 'wmode')
        param.set('value', 'opaque')
        obj.append(param)
        param = etree.Element('param')
        param.set('name', 'allowFullScreen')
        param.set('value', 'true')
        obj.append(param)
        #param = etree.Element('param')
        #param.set('name', 'allowScriptAccess')
        #param.set('value', 'sameDomain')
        #obj.append(param)
        return obj

def makeExtension(configs=None) :
    if configs is None: configs = {}
    return VideoExtension(configs=configs)
