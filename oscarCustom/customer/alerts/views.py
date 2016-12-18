from oscar.apps.customer.alerts.views import ProductAlertListView as CoreProductAlertListView


class ProductAlertListView(CoreProductAlertListView):
    template_name = 'oscar/customer/alerts/alert_list.html'

