from django.test import TestCase
from django.utils import timezone
from puzzle.models import Puzzle
# Create your tests here.


class PuzzleTest(TestCase):
    def setUp(self):
        self.puzzle = Puzzle.objects.create(
            title="test puzzle", size=2, created_at=timezone.now(),
            update_at=timezone.now(), picture_url="test.png", user_id="1abc")

    def test_valid_user(self):
        self.assertIs(Puzzle.objects.filter(pk=1).exists(), True)
