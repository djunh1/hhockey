from oscar.apps.customer.views import AccountAuthView as CoreAccountAuthView


class AccountAuthView(CoreAccountAuthView):
    template_name = 'oscar/customer/login_registration.html'