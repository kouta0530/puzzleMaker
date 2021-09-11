from django.core.exceptions import ValidationError
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
        self.assertEquals(Puzzle.objects.all().count(), 1)

    def test_title_presence(self):
        with self.assertRaises(ValidationError) as e:
            non_title_puzzle = Puzzle(
                title="", size=2, created_at=timezone.now(),
                update_at=timezone.now(), picture_url="test.png",
                user_id="user_2"
            )
            non_title_puzzle.full_clean()

        exception = e.exception
        self.assertEquals(Puzzle.objects.all().count(), 1)
        self.assertEquals(exception.message_dict,
                          {'title': ['This field cannot be blank.']})

    def test_title_over_length_prevent(self):
        with self.assertRaises(ValidationError) as e:
            long_title_puzzle = Puzzle(
                title="a" * 201, size=2, created_at=timezone.now(),
                update_at=timezone.now(), picture_url="test.png",
                user_id="user_2"
            )
            long_title_puzzle.full_clean()

        exception = e.exception
        self.assertEquals(Puzzle.objects.all().count(), 1)
        self.assertEquals(
            exception.message_dict,
            {'title':
             ['Ensure this value has at most 200 characters (it has 201).']})
