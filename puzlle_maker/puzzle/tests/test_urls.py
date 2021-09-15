from django.test import TestCase
from django.urls import reverse, resolve
from puzzle.views import index


class UrlsTest(TestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
