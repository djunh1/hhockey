from oscar.apps.customer.wishlists.views import WishListListView as CoreWishListListView


class WishListListView(CoreWishListListView):
    template_name = 'oscar/customer/wishlists/wishlists_list.html'
