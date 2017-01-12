from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):
    def test_can_open_home_page(self):
        self.browser.get('http://heritage-hockey.com:8000/')
        self.assertIn('Hopewell Hockey', self.browser.title)

    def test_can_read_privacy_policy(self):
        pass

    def test_user_has_questions_goes_to_faq(self):
        pass




