from oscar.apps.customer.views import AccountAuthView as CoreAccountAuthView
from oscar.apps.customer.views import ProfileUpdateView as CoreProfileUpdateView
from oscar.apps.customer.views import ProfileView as CoreProfileView
from oscar.apps.customer.views import OrderHistoryView as CoreOrderHistoryView
from oscar.apps.customer.views import AddressListView as CoreAddressListView
from oscar.apps.customer.views import EmailHistoryView as CoreEmailHistoryView
from oscar.apps.customer.views import ChangePasswordView as CoreChangePasswordView
from oscar.apps.customer.views import ProfileDeleteView as CoreProfileDeleteView
from oscar.apps.customer.views import AddressCreateView as CoreAddressCreateView


class AccountAuthView(CoreAccountAuthView):
    template_name = 'oscar/customer/login_registration.html'


class ProfileView(CoreProfileView):
    template_name = 'oscar/customer/profile/profile.html'


class OrderHistoryView(CoreOrderHistoryView):
    template_name = 'oscar/customer/order/order_list.html'


class AddressListView(CoreAddressListView):
    template_name = 'oscar/customer/address/address_list.html'


class EmailHistoryView(CoreEmailHistoryView):
    template_name = 'oscar/customer/email/email_list.html'


class ChangePasswordView(CoreChangePasswordView):
    template_name = 'oscar/customer/profile/change_password_form.html'


class ProfileDeleteView(CoreProfileDeleteView):
    template_name = 'oscar/customer/profile/profile_delete.html'


class AddressCreateView(CoreAddressCreateView):
    template_name = 'oscar/customer/address/address_form.html'


class ProfileUpdateView(CoreProfileUpdateView):
    template_name = 'oscar/customer/profile/profile_form.html'