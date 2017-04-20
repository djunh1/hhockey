from oscar.apps.customer.alerts.views import ProductAlertListView as CoreProductAlertListView
from oscar.apps.customer.alerts.views import ProductAlertCreateView as CoreProductAlertCreateView

class ProductAlertListView(CoreProductAlertListView):
    template_name = 'oscar/customer/alerts/alert_list.html'


class ProductAlertCreateView(CoreProductAlertCreateView):
    template_name = 'oscar/customer/alerts/form.html'

