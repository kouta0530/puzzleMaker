from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from puzzle.models import Puzzle
from django.utils import timezone


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

    def test_title_logo_url(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        url = self.selenium.find_element_by_tag_name('a').get_attribute('href')
        self.assertEquals(url, self.live_server_url + '/')

    def test_msg_no_posted_puzzle(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        msg = self.selenium.find_element_by_class_name(
            'no-puzzle-data-msg').text
        self.assertEquals(msg, 'パズルが投稿されていません')

    def test_posted_puzzle(self):
        Puzzle.objects.create(
            title='test',
            size=2,
            created_at=timezone.now(),
            update_at=timezone.now(),
            picture_url="test.png",
            user_id="abdg3fh"
        )
        self.selenium.get('%s%s' % (self.live_server_url, '/'))
        msg = self.selenium.find_elements_by_class_name(
            'no-puzzle-data-msg')
        self.assertEquals(msg, [])
