from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import unittest
import sys

class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = "http:// + arg.split('=')[1]"
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        print(self.server_url)
        '''
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)
        '''

    def tearDown(self):
        '''
        self.browser.quit()
        '''

    def test_can_launch_browser_to_home(self):
        '''
        TO DO
        Once webdriver is working without pointing to old firefox binaries, write user tests
        '''
        pass


