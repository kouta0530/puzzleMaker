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

    def check_validation(self):
        with self.assertRaises(ValidationError) as e:
            self.puzzle.full_clean()

        return e.exception

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

    def test_size_under_min_value(self):
        with self.assertRaises(ValidationError) as e:
            smaller_size_puzzle = Puzzle(
                title="smaller puzzle",
                size=1, created_at=timezone.now(), update_at=timezone.now(),
                picture_url="test.png", user_id="user_2")
            smaller_size_puzzle.full_clean()
        exception = e.exception
        expected = {
            'size':
            ['Ensure this value is greater than or equal to 2.']
        }

        self.assertEquals(exception.message_dict, expected)
        self.assertEquals(Puzzle.objects.all().count(), 1)

    def test_size_over_max_value(self):
        self.puzzle.size = 11
        exception = self.check_validation()
        self.assertEquals(exception.message_dict, {
                          'size':
                          ['Ensure this value is less than or equal to 10.']})
