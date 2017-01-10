from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

from hhockeyUser.models import User
from hhockeyUser.forms import UserForm

class AppUserTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(email='jacob@…', password='top_secret')

    def tearDown(self):
        self.user.delete()

    def testProfileString(self):
        '''
        Checks that the default user is active and their name is the email address.
        '''
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(str(self.user), 'jacob@…')
        self.assertEqual(str(self.user.is_active), 'True')

    def test_user_is_not_admin(self):
        '''
        Verifies created user is not a superuser or an admin
        '''
        self.assertEqual(str(self.user.is_superuser), 'False')

    def test_user_can_change_username(self):
        '''
        The user can update their username if they desire.
        '''
        self.user.name = 'dory'
        self.user.save()
        self.assertEqual(str(self.user.name), 'dory')

    def testProfileIsSaved(self):
        self.user.position = 'WING'
        self.user.save()
        self.assertEqual(str(self.user.position), 'WING')

    def test_profile_updated_with_league(self):
        self.user.league = 'college'
        self.user.save()
        self.assertEqual(str(self.user.league), 'college')

class AppUserFormTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(email='jacob@…', password='top_secret')

    def tearDown(self):
        self.user.delete()

    def test_form_has_correct_fields(self):
        '''
        Checks to see if all the needed fields populate
        '''
        form = UserForm(self.user)
        self.assertTrue(form.fields['first_name'])
        self.assertTrue(form.fields['last_name'])
        self.assertTrue(form.fields['email'])
        self.assertTrue(form.fields['birth_date'])
        self.assertTrue(form.fields['league'])
        self.assertTrue(form.fields['position'])
