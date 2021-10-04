from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class IntegrationTest(StaticLiveServerTestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")

        self.selenium = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options
        )

    def tearDown(self):
        self.selenium.quit()

    def test_get_index_page(self):
        self.selenium.get('http://127.0.0.1:8000')
        e = self.selenium.find_element_by_tag_name('head')
        print('test', e.text)
