from django.test import TestCase
from puzzle.helper import create_index


class HelperFunctionTest(TestCase):
    def test_create_index_mod_zero(self):
        self.assertEquals(create_index(30, 30), [i+1 for i in range(1)])

    def test_create_index(self):
        self.assertEquals(create_index(31, 30), [i+1 for i in range(2)])
