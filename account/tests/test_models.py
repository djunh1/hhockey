from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User

class ModelTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='Eric_Seager', email='jacob@…', password='top_secret')

    def tearDown(self):
        self.user.delete()

    def testProfileString(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(str(self.user), 'Eric_Seager')

    def testProfileIsCreated(self):
        self.assertEqual(hasattr(self.user, 'profile'), True)

    def testProfileIsSaved(self):
        self.user.profile.position = 'WING'
        self.user.save()
        self.assertEqual(str(self.user.profile.position), 'WING')




