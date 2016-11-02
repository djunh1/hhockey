from django.contrib import messages
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.test.client import Client
from django.urls import reverse


from account.forms import UserRegistrationForm, UserEditForm, ProfileEditForm

'''
TO DO

Refactor code -  make functions to supply post data.
'''
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
        response = self.client.post(reverse('account:register'),
                                    {
                                        'username': 'testuser',
                                        'password': '6510656516061510',
                                        'password2': '6510656516061510',
                                    })
        self.assertTrue(User.objects.all()[0].is_authenticated())
        self.assertTrue(User.objects.all()[0])
        self.assertTemplateUsed(response, 'account/register_done.html')
        self.assertEqual(response.status_code, 200)

    def test_user_not_created_with_bad_passwords(self):
        self.client.post(reverse('account:register'),
                                    {
                                        'username': 'testuser',
                                        'password': '6510656516061510',
                                        'password2': '6510656516061511',
                                    })
        self.assertFalse(User.objects.all())

    def test_user_not_created_with_no_username(self):
        self.client.post(reverse('account:register'),
                                    {
                                        'username': '',
                                        'password': '6510656516061510',
                                        'password2': '6510656516061510',
                                    })
        self.assertFalse(User.objects.all())


class EditProfileTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='Eric_Seager', email='jacob@…', password='top_secret')
        self.user2 = User.objects.create_user(username='dry', email='dry@…', password='top_secret2')

    def test_login_required_to_edit(self):
        response = self.client.get(reverse('account:edit_profile'))
        self.assertRedirects(response, reverse('account:login')+'?next='+reverse('account:edit_profile'))

    def test_edit_profile_renders_page(self):
        self.client.login(username='Eric_Seager', password='top_secret')
        response = self.client.get(reverse('account:edit_profile'))
        self.assertTemplateUsed(response, 'account/editProfile.html')
        self.assertEqual(response.status_code, 200)

    def test_correct_forms_rendered(self):
        self.client.login(username='Eric_Seager', password='top_secret')
        response = self.client.get(reverse('account:edit_profile'))
        self.assertIsInstance(response.context['user_form'], UserEditForm)
        self.assertIsInstance(response.context['profile_form'], ProfileEditForm)

    def test_edit_profile_post_saves_userforms(self):
        self.client.login(username='Eric_Seager', password='top_secret')
        user_form_data = {'first_name': 'WarrenBuffet', 'email': 'wb@test.com'}
        response = self.client.post(reverse('account:register'),
                                    user_form_data)
        self.assertTrue(self.user.profile)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(messages.success)

    def test_edit_profile_post_saves_profileforms(self):
        self.client.login(username='Eric_Seager', password='top_secret')
        profile_form_data = {'league': 'TRAVEL', 'position': 'WING'}
        response = self.client.post(reverse('account:register'),
                                    profile_form_data)
        self.assertTrue(self.user.profile)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(messages.success)

    def test_edit_profile_form_not_valid(self):
        pass
        '''
        Currently, none of these forms require input thus will always pass as valid
        upon submission.  If any new fields are added and are required, write this test
        to invalid forms are handled properly.
        '''
