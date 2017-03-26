from django.test import TestCase, RequestFactory
from django.contrib.auth import authenticate
from django.conf import settings

from oscarCustom.checkout.views import PaymentDetailsView
from oscarCustom.checkout.facade import Facade

import stripe

from hhockeyUser.models import User

class AppPaymentTest(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def loginToClient(self):
        self.user = User.objects.create(username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('hello')
        self.user.save()
        self.user = authenticate(username='testuser', password='hello')
        login = self.client.login(username='testuser', password='hello')
        return login

    def test_payment_gateway_renders(self):
        pass

