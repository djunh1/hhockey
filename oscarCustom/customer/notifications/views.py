from oscar.apps.customer.notifications.views import NotificationListView as CoreNotificationListView



class NotificationListView(CoreNotificationListView):
    template_name = 'oscar/customer/notifications/list.html'


class InboxView(NotificationListView):
    list_type = 'inbox'

class ArchiveView(NotificationListView):
    list_type = 'archive'