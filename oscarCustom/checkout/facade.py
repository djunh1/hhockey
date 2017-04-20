from django.conf import settings
from oscar.apps.payment.exceptions import UnableToTakePayment, InvalidGatewayRequestError, GatewayError

import stripe


class Facade(object):
    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY

    @staticmethod
    def get_decline_message(error):
        return 'The transaction was declined by the bank -  Please check your card details and try again'

    @staticmethod
    def get_error_message(error):
        return 'We encountered an error while communicating with the payment gateway.'

    @staticmethod
    def get_api_message(error):
        return 'We were unable to connect to Stripe.  Please try again later.'

    @staticmethod
    def get_rate_error(error):
        return 'Too many requests made to this API.  Please try again later.'

    @staticmethod
    def get_invalid_request_error(error):
        return 'Invalid parameters were supplied to the Stripe API'

    @staticmethod
    def get_auth_error(error):
        return 'We were unable to authenticate our system with Stripe.  Please try again later.'



    def charge(self,
               order_number,
               total,
               card,
               currency=settings.STRIPE_CURRENCY,
               description=None,
               metadata=None,
               **kwargs):

        try:
            return stripe.Charge.create(
                amount=(total.incl_tax * 100).to_integral_value(),
                currency=currency,
                card=card,
                description=description,
                metadata=(metadata or {'order_number': order_number}),
                **kwargs).id

        except stripe.error.CardError as e:
            raise UnableToTakePayment(self.get_decline_message(e))

        except stripe.error.StripeError as e:
            raise InvalidGatewayRequestError(self.get_error_message(e))

        except stripe.error.APIConnectionError as e:
            raise UnableToTakePayment(self.get_api_message(e))

        except stripe.error.InvalidRequestError as e:
            raise InvalidGatewayRequestError(self.get_invalid_request_error(e))

        except stripe.error.RateLimitError as e:
            raise GatewayError(self.get_rate_error(e))

        except stripe.error.AuthenticationError as e:
            raise GatewayError(self.get_auth_error(e))

        except Exception as e:
            raise UnableToTakePayment(self.get_error_message(e))


