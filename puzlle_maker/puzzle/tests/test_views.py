from django.test import TestCase, Client


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_index_page(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
