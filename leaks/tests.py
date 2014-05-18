import unittest
from ltmo.models import Leak

class TestLeak (unittest.TestCase):

    def setUp(self):
        self.mock_content = {
		'title': 'This is a test leak',
		'description': '**some** [Markdown](http://markdown.org) text.',
		'author':'pindonga'
        }
        self.expected_content = {
		'title': 'This is a test leak',
		'description': '**some** [Markdown](http://markdown.org) text.',
		'author': 'pindonga',
		'rendered': u'''<p><strong>some</strong> <a href="http://markdown.org">Markdown</a> text.</p>'''
        }
        self.leak = Leak.objects.create(**self.mock_content)
    def test_MarkdownOk(self):
        self.assertEquals(self.leak.rendered, self.expected_content['rendered'])
