import unittest
from ltmo.models import Leak

class TestLeak (unittest.TestCase):

    def setUp(self):
        self.mock_content = '**some** [Markdown](http://markdown.org) text.'
        self.leak = Leak.objects.create(
            title='Prueba',
            description=self.mock_content
            )
    def test_MarkdownOk(self):
        self.assertEquals(self.description, self.mock_content)

