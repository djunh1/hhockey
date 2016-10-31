from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.test.client import Client
from django.urls import reverse


from account.forms import UserRegistrationForm

class UserLoginTest(TestCase):
    def test_login_renders_page(self):
        response = self.client.get(reverse('account:login'))
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_edit_denies_anonymous(self):
        response = self.client.get(reverse('account:edit'))
        self.assertRedirects(response, reverse('account:login')+'?next='+reverse('account:edit'))

class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_renders_page(self):
        response = self.client.get(reverse('account:register'))
        self.assertTemplateUsed(response, 'account/register.html')

    def test_register_form_is_correct(self):
        response = self.client.get(reverse('account:register'))
        self.assertIsInstance(response.context['user_form'], UserRegistrationForm)

    def test_login(self):
        self.client.post(reverse('account:register'),
                                    {
                                        'username': 'testuser',
                                        'password': '6510656516061510',
                                        'password2': '6510656516061510',
                                    })
        self.assertTrue(User.objects.all()[0].is_authenticated())