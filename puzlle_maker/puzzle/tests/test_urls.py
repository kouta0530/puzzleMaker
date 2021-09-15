from django.test import TestCase
from django.urls import reverse, resolve
from puzzle.views import index, get_puzzle_data


class UrlsTest(TestCase):
    def test_index_url(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)

    def test_get_additional_puzzle_url(self):
        url = reverse('get puzzle data', kwargs={'id': 1})
        self.assertEqual(resolve(url).func, get_puzzle_data)
