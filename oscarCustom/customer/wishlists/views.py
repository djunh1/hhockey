from oscar.apps.customer.wishlists.views import WishListListView as CoreWishListListView
from oscar.apps.customer.wishlists.views import WishListCreateView as CoreWishListCreateView
from oscar.apps.customer.wishlists.views import WishListDetailView as CoreWishListDetailView

class WishListListView(CoreWishListListView):
    template_name = 'oscar/customer/wishlists/wishlists_list.html'


class WishListCreateView(CoreWishListCreateView):
    template_name = 'oscar/customer/wishlists/wishlists_form.html'


class WishListDetailView(CoreWishListDetailView):
    template_name = 'oscar/customer/wishlists/wishlists_detail.html'
