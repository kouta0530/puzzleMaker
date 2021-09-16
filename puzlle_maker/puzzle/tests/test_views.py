from django.test import TestCase, Client
from django.urls import reverse, resolve
from puzzle.models import Puzzle
from django.utils import timezone


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.puzzle = Puzzle.objects.create(
            title="test",
            size=2,
            created_at=timezone.now(),
            update_at=timezone.now(),
            picture_url="test.png",
            user_id="abdg3fh"
        )

    def test_get_index_page(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    def test_get_additional_puzzle_data(self):
        url = reverse('get puzzle data', kwargs={'id': 0})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
