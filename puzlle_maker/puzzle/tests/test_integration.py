from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class IntegrationTest(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--headless")
        options.add_argument("--disable-dev-shm-usage")
        cls.host = 'web'
        cls.selenium = webdriver.Remote(
            command_executor='http://selenium:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options
        )
        cls.selenium.implicitly_wait(5)
        super(IntegrationTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(IntegrationTest, cls).tearDownClass()

    def test_get_index_page(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        url = self.selenium.find_element_by_tag_name('a').get_attribute('href')
        self.assertEquals(url, self.live_server_url + '/')
