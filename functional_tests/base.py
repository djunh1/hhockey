from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import os

os.environ["PATH"] += ":/Users/djunh/bin"


class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        firefox_capabilities = DesiredCapabilities.FIREFOX
        firefox_capabilities['marionette'] = True
        #firefox_capabilities['binary'] = '/Users/djunh/bin'
        driver = webdriver.Firefox(capabilities=firefox_capabilities)

    def testPageTitle(self):
        self.browser.get('http://www.google.com')
        self.assertIn('Google', self.browser.title)

if __name__ == '__main__':
    unittest.main(verbosity=2)
