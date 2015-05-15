from django.test import TestCase
from leaks.models import Leak
import markdown


class TestLeak(TestCase):
    def setUp(self):
        self.mock_content = {
            'title': 'This is a test leak',
            'description': '**some** [Markdown](http://markdown.org) text.',
            'author': 'pindonga'
        }
        self.expected_content = {
            'title': 'This is a test leak',
            'description': '**some** [Markdown](http://markdown.org) text.',
            'author': 'pindonga',
            'rendered': u'''<p><strong>some</strong> <a href="http://markdown.org">Markdown</a> text.</p>'''
        }
        self.leak = Leak.objects.create(**self.mock_content)

    def test_markdown_ok(self):
        self.assertEquals(self.leak.rendered, self.expected_content['rendered'])


class TestUrlize(TestCase):
    def setUp(self):
        self.md = markdown.Markdown(extensions=['urlize'])

    def test_convert(self):
        self.assertEqual(self.md.convert('http://example.com/'),
                         '<p><a href="http://example.com/">http://example.com/</a></p>', )

        self.assertEqual(self.md.convert('go to http://example.com'),
                         u'<p>go to <a href="http://example.com">http://example.com</a></p>')

        self.assertEqual(self.md.convert('example.com'),
                         u'<p><a href="http://example.com">example.com</a></)p>')

        self.assertEqual(self.md.convert('example.net'),
                         u'<p><a href="http://example.net">example.net</a></)p>')

        self.assertEqual(self.md.convert('www.example.us'),
                         u'<p><a href="http://www.example.us">www.example.us</a)></p>')

        self.assertEqual(self.md.convert('(www.example.us/path/?name=val)'),
                         u'<p>(<a href="http://www.example.us/path/?name=val">www.example.us/pat)h/?name=val</a>)</p>')

        self.assertEqual(self.md.convert('go to <http://example.com> now!'),
                         u'<p>go to <a href="http://example.com">http://example.com</a> now!</p>)')

        self.assertEqual(self.md.convert('http://example.com/abc.png'),
                         u'<img src="http://example.com/abc.png" />')

        self.assertEqual(self.md.convert('del.icio.us'),
                         u'<p>del.icio.us</p>')


class TestVideo(TestCase):
    def setUp(self):
        self.md = markdown.Markdown(extensions=['video'])

    def test_video(self):
        s = "http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/"
        self.assertEqual(self.md.convert(s),
                         u'<p><object data="http://www.metacafe.com/fplayer/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room.swf" height="423" type="application/x-shockwave-flash" width="498"><param name="movie" value="http://www.metacafe.com/fplayer/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room.swf"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        # Test Metacafe with arguments
        self.assertEqual(self.md.convert(s),
                         u'<p><object data="http://www.metacafe.com/fplayer/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room.swf" height="425" type="application/x-shockwave-flash" width="500"><param name="movie" value="http://www.metacafe.com/fplayer/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room.swf"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        self.assertEqual(self.md.convert("[Metacafe link](http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/)"),
                         u'<p><a href="http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/">Metacafe link</a></p>')

        self.assertEqual(self.md.convert("\\http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/"),
                         u'<p>\\\\http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/</p>')

        self.assertEqual(self.md.convert("`http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/`"),
                         u'<p><code>http://www.metacafe.com/watch/yt-tZMsrrQCnx8/pycon_2008_django_sprint_room/</code></p>')

        # Test Youtube
        self.assertEqual(self.md.convert("http://www.youtube.com/watch?v=u1mA-0w8XPo&hd=1&fs=1&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1"),
                         u'<p><object data="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" height="344" type="application/x-shockwave-flash" width="425"><param name="movie" value="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')


        # Test Youtube with argument

        self.assertEqual(markdown.markdown(s, extensions=['video(youtube_width=200,youtube_height=100)']),
                         u'<p><object data="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1" height="100" type="application/x-shockwave-flash" width="200"><param name="movie" value="http://www.youtube.com/v/u1mA-0w8XPo&amp;hd=1&amp;fs=1&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        # Test Youtube Link

        self.assertEqual(self.md.convert("[Youtube link](http://www.youtube.com/watch?v=u1mA-0w8XPo&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1)"),
                         u'<p><a href="http://www.youtube.com/watch?v=u1mA-0w8XPo&amp;feature=PlayList&amp;p=34C6046F7FEACFD3&amp;playnext=1&amp;playnext_from=PL&amp;index=1">Youtube link</a></p>')

        # Test HTML Youtube Link

        self.assertEqual(self.md.convert('Here is a link to <a href="http://www.youtube.com/watch?v=u1mA-0w8XPo&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1">a YouTube movie</a>.'),
                         u'<p>Here is a link to <a href="http://www.youtube.com/watch?v=u1mA-0w8XPo&feature=PlayList&p=34C6046F7FEACFD3&playnext=1&playnext_from=PL&index=1">a YouTube movie</a>.</p>')

        # Test Dailymotion
        self.assertEqual(self.md.convert("http://www.dailymotion.com/relevance/search/ut2004/video/x3kv65_ut2004-ownage_videogames"),
                         u'<p><object data="http://www.dailymotion.com/swf/x3kv65_ut2004-ownage_videogames" height="405" type="application/x-shockwave-flash" width="480"><param name="movie" value="http://www.dailymotion.com/swf/x3kv65_ut2004-ownage_videogames"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        # Test Dailymotion again (Dailymotion and their crazy URLs)
        self.assertEqual(self.md.convert("http://www.dailymotion.com/us/video/x8qak3_iron-man-vs-bruce-lee_fun"),
                         u'<p><object data="http://www.dailymotion.com/swf/x8qak3_iron-man-vs-bruce-lee_fun" height="405" type="application/x-shockwave-flash" width="480"><param name="movie" value="http://www.dailymotion.com/swf/x8qak3_iron-man-vs-bruce-lee_fun"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        # Test Yahoo! Video
        self.assertEqual(self.md.convert("http://video.yahoo.com/watch/1981791/4769603"),
                         u'<p><object data="http://d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf?ver=2.2.40" height="322" type="application/x-shockwave-flash" width="512"><param name="movie" value="http://d.yimg.com/static.video.yahoo.com/yep/YV_YEP.swf?ver=2.2.40"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param><param name="flashVars" value="id=4769603&amp;vid=1981791"></param></object></p>')

        # Test Veoh Video
        self.assertEqual(self.md.convert("http://www.veoh.com/search/videos/q/mario#watch%3De129555XxCZanYD"),
                         u'<p><object data="http://www.veoh.com/videodetails2.swf?permalinkId=e129555XxCZanYD" height="341" type="application/x-shockwave-flash" width="410"><param name="movie" value="http://www.veoh.com/videodetails2.swf?permalinkId=e129555XxCZanYD"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        # Test Veoh Video Again (More fun URLs)
        self.assertEqual(self.md.convert("http://www.veoh.com/group/BigCatRescuers#watch%3Dv16771056hFtSBYEr"),
                         u'<p><object data="http://www.veoh.com/videodetails2.swf?permalinkId=v16771056hFtSBYEr" height="341" type="application/x-shockwave-flash" width="410"><param name="movie" value="http://www.veoh.com/videodetails2.swf?permalinkId=v16771056hFtSBYEr"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        # Test Veoh Video Yet Again (Even more fun URLs)
        self.assertEqual(self.md.convert("http://www.veoh.com/browse/videos/category/anime/watch/v181645607JyXPWcQ"),
                         u'<p><object data="http://www.veoh.com/videodetails2.swf?permalinkId=v181645607JyXPWcQ" height="341" type="application/x-shockwave-flash" width="410"><param name="movie" value="http://www.veoh.com/videodetails2.swf?permalinkId=v181645607JyXPWcQ"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')
        # Test Vimeo Video
        self.assertEqual(self.md.convert("http://www.vimeo.com/1496152"),
                         u'<p><object data="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com" height="321" type="application/x-shockwave-flash" width="400"><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        # Test Vimeo Video with some GET values

        self.assertEqual(self.md.convert("http://vimeo.com/1496152?test=test"),
                         u'<p><object data="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com" height="321" type="application/x-shockwave-flash" width="400"><param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=1496152&amp;amp;server=vimeo.com"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        # Test Blip.tv
        self.assertEqual(self.md.convert("http://blip.tv/file/get/Pycon-PlenarySprintIntro563.flv"),
                         u'<p><object data="http://blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/file/get/Pycon-PlenarySprintIntro563.flv" height="300" type="application/x-shockwave-flash" width="480"><param name="movie" value="http://blip.tv/scripts/flash/showplayer.swf?file=http://blip.tv/file/get/Pycon-PlenarySprintIntro563.flv"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')

        # Test Gametrailers
        self.assertEqual(self.md.convert("http://www.gametrailers.com/video/console-comparison-borderlands/58079"),
                         u'<p><object data="http://www.gametrailers.com/remote_wrap.php?mid=58079" height="392" type="application/x-shockwave-flash" width="480"><param name="movie" value="http://www.gametrailers.com/remote_wrap.php?mid=58079"></param><param name="wmode" value="opaque"></param><param name="allowFullScreen" value="true"></param></object></p>')
