from django.test import TestCase, RequestFactory
from django.contrib.auth import authenticate

from oscarCustom.promotions.views import HomeView
from oscarCustom.basket.views import BasketView
from oscarCustom.catalogue.views import CatalogueView, ProductCategoryView, ProductDetailView
from oscarCustom.catalogue.reviews.views import CreateProductReview, ProductReviewList, ProductReviewDetail
from oscarCustom.checkout.views import IndexView, ShippingAddressView, PaymentDetailsView, ThankYouView, UserAddressUpdateView
from oscarCustom.customer.views import AccountAuthView, AddressDeleteView, ProfileView, OrderHistoryView, \
    AddressListView, EmailHistoryView, ChangePasswordView, ProfileDeleteView, AddressCreateView, ProfileUpdateView


from hhockeyUser.models import User
from hhockeyUser.forms import UserForm


class AppCustomViews(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(email='jacob@…', password='top_secret')

    def tearDown(self):
        self.user.delete()

    def loginToClient(self):
        self.user = User.objects.create(username='testuser', password='12345', is_active=True, is_staff=True, is_superuser=True)
        self.user.set_password('hello')
        self.user.save()
        self.user = authenticate(username='testuser', password='hello')
        login = self.client.login(username='testuser', password='hello')
        return login

    def test_promotions_views(self):
        request = self.client.get('/shop/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(HomeView.template_name, 'oscar/promotions/home.html')

    def test_basket_view_template(self):
        r
    def test_catalogue_view_templates(self):
        request = self.client.get('/shop/catalogue/')
        self.assertEqual(request.status_cequest = self.client.get('/shop/basket/')
        self.assertTemplateUsed(request, 'oscar/basket/basket.html')
ode, 200)
        self.assertTemplateUsed(request, 'oscar/catalogue/browse.html')
        self.assertEqual(ProductCategoryView.template_name, 'oscar/catalogue/category.html')
        self.assertEqual(ProductDetailView.template_folder, 'oscar/catalogue')

    def test_catalogue_review_templates(self):
        self.assertEqual(CreateProductReview.template_name, 'oscar/catalogue/reviews/review_form.html')
        self.assertEqual(ProductReviewList.template_name, 'oscar/catalogue/reviews/review_list.html')
        self.assertEqual(ProductReviewDetail.template_name, 'oscar/catalogue/reviews/review_detail.html')


    def test_checkout_view_templates(self):
        request = self.client.get('/shop/checkout/')
        self.assertEqual(request.status_code, 302)
        self.assertEqual(IndexView.template_name, 'oscar/checkout/gateway.html')
        self.assertEqual(ShippingAddressView.template_name, 'oscar/checkout/shipping_address.html')
        self.assertEqual(PaymentDetailsView.template_name, 'oscar/checkout/payment_details.html')
        self.assertEqual(PaymentDetailsView.template_name_preview, 'oscar/checkout/preview.html')
        self.assertEqual(ThankYouView.template_name, 'oscar/checkout/thank_you.html')
        self.assertEqual(UserAddressUpdateView.template_name, 'oscar/checkout/user_address_form.html')

    def test_basket_view_templates(self):
        request = self.client.get('/shop/basket/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(BasketView.template_name, 'oscar/basket/basket.html')

    def test_customer_view_templates(self):
        request = self.client.get('/shop/accounts/login/')
        self.assertEqual(request.status_code, 200)
        self.assertTemplateUsed(request, 'oscar/customer/login_registration.html')

    def test_logged_in_user_profile_templates(self):
        request = self.factory.get('/shop/accounts/profile/')
        request.user = self.user
        response = ProfileView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ProfileView.template_name, 'oscar/customer/profile/profile.html')

    def test_logged_in_user_orderHistory_templates(self):
        request = self.factory.get('/shop/accounts/orders/')
        request.user = self.user
        response = OrderHistoryView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(OrderHistoryView.template_name, 'oscar/customer/order/order_list.html')

    def test_logged_in_user_addressBook_templates(self):
        request = self.factory.get('/shop/accounts/addresses/')
        request.user = self.user
        response = AddressListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AddressListView.template_name, 'oscar/customer/address/address_list.html')

    def test_logged_in_user_emailHistory_templates(self):
        request = self.factory.get('/shop/accounts/emails/')
        request.user = self.user
        response = EmailHistoryView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(EmailHistoryView.template_name, 'oscar/customer/email/email_list.html')

    def test_logged_in_user_password_change_templates(self):
        request = self.factory.get('/shop/accounts/change-password/')
        request.user = self.user
        response = ChangePasswordView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ChangePasswordView.template_name, 'oscar/customer/profile/change_password_form.html')

    def test_logged_in_user_profile_delete_templates(self):
        request = self.factory.get('/shop/accounts/profile/delete/')
        request.user = self.user
        response = ProfileDeleteView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ProfileDeleteView.template_name, 'oscar/customer/profile/profile_delete.html')

    def test_logged_in_user_address_create_templates(self):
        request = self.factory.get('/shop/accounts/addresses/add/')
        request.user = self.user
        response = AddressCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(AddressCreateView.template_name, 'oscar/customer/address/address_form.html')

    def test_logged_in_user_profile_update_templates(self):
        request = self.factory.get('/shop/accounts/profile/edit/')
        request.user = self.user
        response = ProfileUpdateView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ProfileUpdateView.template_name, 'oscar/customer/profile/profile_form.html')

    def test_logging_in_user_updates_with_correct_form(self):
        '''
        Ensure that the correct form is being rendered when the user wants to edit their profile
        '''
        login = self.loginToClient()
        response = self.client.get('/shop/accounts/profile/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], UserForm)

