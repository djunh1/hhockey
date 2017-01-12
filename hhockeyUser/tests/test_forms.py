from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from hhockeyUser.forms import UserForm
from hhockeyUser.models import User

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

    def test_form_valid(self):
        form_data = {'first_name': 'Dory',
                     'last_name': 'M.',
                     'email': 'd@test.com',
                     'birth_date': '1/1/1990',
                     'league': 'COLLEGE',
                     'position': 'WING'}
        form = UserForm(self.user, data=form_data)
        self.assertEqual(form.is_valid(), True)

    def test_form_not_valid_for_date(self):
        form_data = {'first_name': 'Dory', 'birth_date': 'drystrbry'}
        form = UserForm(self.user, data=form_data)
        self.assertEqual(form.is_valid(), False)
