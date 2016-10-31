from django import forms
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

from account.forms import LoginForm, UserRegistrationForm, SignupForm, UserEditForm, ProfileEditForm

class LoginFormsTest(TestCase):
    def test_login_form_no_password(self):
        form_data = {'username': 'WarrenBuffet', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_login_form_password(self):
        form_data = {'username': 'WarrenBuffet', 'password': 'goWellsFargo12'}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_validation_form_blank_items(self):
        form_data = {'username': '', 'password': ''}
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ["Please Select a Valid Username"])
        self.assertEqual(form.errors['password'], ["Please Select a Valid Password"])


class UserRegistrationFormsTest(TestCase):
    def test_password_checker(self):
        form_data = {'username': 'WarrenBuffet'}
        form = UserRegistrationForm(data=form_data)
        form.cleaned_data = {'password': 'goWellsFargo12', 'password2': 'goWellsFargo11'}
        self.assertRaises(forms.ValidationError, form.clean_password2)

    def test_form_model(self):
        form_data = {'username': '', 'password': 'goWellsFargo12', 'password2': 'goWellsFargo12'}
        form = UserRegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())


class SignupFormFormsTest(TestCase):
    def test_profile_saves(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='Eric_Seager', email='jacob@…', password='top_secret')
        form = SignupForm(self.user)
        self.assertTrue(self.user.profile)


class UserAndProfileFOrmsTest(TestCase):
    def test_user_form_fields(self):
        form = UserEditForm()
        self.assertTrue(form.fields['first_name'])
        self.assertTrue(form.fields['email'])

    def test_profile_form_fields(self):
        form = ProfileEditForm()
        self.assertTrue(form.fields['birth_date'])
        self.assertTrue(form.fields['league'])
        self.assertTrue(form.fields['position'])

