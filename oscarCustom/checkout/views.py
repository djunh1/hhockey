from django.conf import settings
from django.shortcuts import redirect
from oscar.core.loading import get_model
from django import forms
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from oscar.apps.payment import models

from oscar.apps.checkout.views import ShippingAddressView as CoreShippingAddressView
from oscar.apps.checkout.views import IndexView as CoreIndexView
from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView
from oscar.apps.checkout.views import ThankYouView as CoreThankYouView
from oscar.apps.checkout.views import UserAddressUpdateView as CoreUserAddressUpdateView
from oscar.apps.checkout.views import ShippingMethodView as CoreShippingMethodView
from oscar.apps.payment.models import SourceType, Source
from oscar.apps.order.models import ShippingAddress
from oscar.apps.address.models import UserAddress

from oscarCustom.checkout.forms import StripeTokenForm
from oscarCustom.checkout.facade import Facade

import pprint


SourceType = get_model('payment', 'SourceType')
Source = get_model('payment', 'Source')

pp = pprint.PrettyPrinter(indent=4)

class IndexView(CoreIndexView):
    template_name = 'oscar/checkout/gateway.html'


class ShippingAddressView(CoreShippingAddressView):
    template_name = 'oscar/checkout/shipping_address.html'

class ShippingMethodView(CoreShippingMethodView):
    pass
    '''
    def get_success_response(self):
        #If different solution is needed, change this redirect to the payment details, and load a bankcard form.
        return redirect('checkout:preview')
    '''

class PaymentDetailsView(CorePaymentDetailsView):
    template_name = 'oscar/checkout/payment_details.html'
    template_name_preview = 'oscar/checkout/preview.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PaymentDetailsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        if self.preview:
            ctx['stripe_token_form'] = StripeTokenForm(self.request.POST)
            ctx['order_total_incl_tax_cents'] = (ctx['order_total'].incl_tax * 100).to_integral_value()
        else:
            ctx['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return ctx

    def handle_payment(self, order_number, total, **kwargs):
        facade = Facade()
        stripe_ref = facade.charge(
            order_number,
            total,
            card=self.request.POST['stripeToken'],
            description=self.payment_description(order_number, total, **kwargs),
            metadata=self.payment_metadata(order_number, total, **kwargs))



        source_type, __ = models.SourceType.objects.get_or_create(name='PAYMENT_METHOD_STRIPE')
        source = models.Source(
            source_type=source_type,
            currency=settings.STRIPE_CURRENCY,
            amount_allocated=total.incl_tax,
            amount_debited=total.incl_tax,
            reference=stripe_ref)
        self.add_payment_source(source)

        pp.pprint(source)

        self.add_payment_event('PAYMENT_EVENT_PURCHASE', total.incl_tax)

    def payment_description(self, order_number, total, **kwargs):
        return self.request.POST['stripeEmail']

    def payment_metadata(self, order_number, total, **kwargs):
        return {'order_number': order_number}


class ThankYouView(CoreThankYouView):
    template_name = 'oscar/checkout/thank_you.html'


class UserAddressUpdateView(CoreUserAddressUpdateView):
    template_name = 'oscar/checkout/user_address_form.html'