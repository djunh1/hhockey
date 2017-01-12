from .base import FunctionalTest
from hhockeyUser.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
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


class UserLoggingIn(FunctionalTest):
    def test_user_can_login(self):
        user = User.objects.create_user(email='ericSeager@unassisted.com', password='123456789')
        request = self.client.request().wsgi_request
        userLogin = authenticate(username='ericSeager@unassisted.com', password='123456789')
        auth.login(request, userLogin)

    def test_user_decides_to_view_cart(self):
        self.browser.get('http://heritage-hockey.com:8000/')
        navbar = self.browser.find_element_by_css_selector('.navbar-collapse')
        self.assertIn('VIEW CART', navbar.text)

    def test_user_logs_out_and_returns_home(self):
        pass



