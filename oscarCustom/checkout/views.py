from oscar.apps.checkout.views import ShippingAddressView as CoreShippingAddressView
from oscar.apps.checkout.views import IndexView as CoreIndexView
from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView
from oscar.apps.checkout.views import ThankYouView as CoreThankYouView
from oscar.apps.checkout.views import UserAddressUpdateView as CoreUserAddressUpdateView


class IndexView(CoreIndexView):
    template_name = 'oscar/checkout/gateway.html'


class ShippingAddressView(CoreShippingAddressView):
    template_name = 'oscar/checkout/shipping_address.html'


class PaymentDetailsView(CorePaymentDetailsView):
    template_name = 'oscar/checkout/payment_details.html'
    template_name_preview = 'oscar/checkout/preview.html'


class ThankYouView(CoreThankYouView):
    template_name = 'oscar/checkout/thank_you.html'


class UserAddressUpdateView(CoreUserAddressUpdateView):
    template_name = 'oscar/checkout/user_address_form.html'