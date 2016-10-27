from django.test import TestCase

class AppTesting(TestCase):
    def test_app_label(self):
        '''
        The app label is changed so the settings file ( Installed apps) does not
        break when two apps with the same name exist.
        '''
        self.assertEqual(1,2)