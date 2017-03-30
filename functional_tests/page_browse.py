from .base import FunctionalTest
from hhockeyUser.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from django.core.urlresolvers import reverse

domain_name = 'http://localhost:8000'

class NewVisitorTest(FunctionalTest):
    def test_can_open_home_page(self):
        self.browser.get(''.join([domain_name, '']))
        self.assertIn('Hopewell Hockey', self.browser.title)

    def test_can_read_privacy_policy(self):
        self.browser.get(''.join([domain_name, '/privacy']))
        self.assertIn('Privacy Policy', self.browser.title)

    def test_can_reviews_terms_and_conditions(self):
        self.browser.get(''.join([domain_name, '/terms']))
        self.assertIn('Terms and Conditions', self.browser.title)

    def test_user_has_questions_goes_to_faq(self):
        '''
        User can navigate to the FAQ and check questions.  The accordian opens or closes as needed.
        Returns:

        '''
        self.browser.get(''.join([domain_name, '/faq']))
        self.assertIn('F.A.Q', self.browser.title)
        self.browser.find_element_by_xpath("//a[contains(@href,'#accordion-2')]").click()
        self.assertTrue(self.browser.find_elements_by_class_name('in'))
        self.browser.find_element_by_xpath("//a[contains(@href,'#accordion-2')]").click()
        self.assertFalse(self.browser.find_elements_by_class_name('in'))



class UserLoggingIn(FunctionalTest):
    def test_user_can_login(self):
        user = User.objects.create_user(email='ericSeager@unassisted.com', password='123456789')
        request = self.client.request().wsgi_request
        userLogin = authenticate(username='ericSeager@unassisted.com', password='123456789')
        auth.login(request, userLogin)

class UserAndTheShop(FunctionalTest):
    def test_user_goes_to_shop(self):
        '''
        User goes to shop and sees a good deal.
        '''
        self.browser.get(''.join([domain_name, '/shop/']))
        self.assertTrue(self.browser.find_element_by_class_name('widget-promo'))


