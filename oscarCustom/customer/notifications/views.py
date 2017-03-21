from oscar.apps.customer.notifications.views import NotificationListView as CoreNotificationListView
from oscar.apps.customer.notifications.views import DetailView as CoreDetailView


class DetailView(CoreDetailView):
    template_name = 'oscar/customer/notifications/detail.html'

class NotificationListView(CoreNotificationListView):
    template_name = 'oscar/customer/notifications/list.html'


class InboxView(NotificationListView):
    list_type = 'inbox'

class ArchiveView(NotificationListView):
    list_type = 'archive'