from oscar.apps.customer.wishlists.views import WishListListView as CoreWishListListView
from oscar.apps.customer.wishlists.views import WishListCreateView as CoreWishListCreateView
from oscar.apps.customer.wishlists.views import WishListDetailView as CoreWishListDetailView
from oscar.apps.customer.wishlists.views import WishListUpdateView as CoreWishListUpdateView
from oscar.apps.customer.wishlists.views import WishListDeleteView as CoreWishListDeleteView
from oscar.apps.customer.wishlists.views import WishListRemoveProduct as CoreWishListRemoveProduct

class WishListListView(CoreWishListListView):
    template_name = 'oscar/customer/wishlists/wishlists_list.html'


class WishListDeleteView(CoreWishListDeleteView):
    template_name = 'oscar/customer/wishlists/wishlists_delete.html'

class WishListCreateView(CoreWishListCreateView):
    template_name = 'oscar/customer/wishlists/wishlists_form.html'


class WishListDetailView(CoreWishListDetailView):
    template_name = 'oscar/customer/wishlists/wishlists_detail.html'

class WishListRemoveProduct(CoreWishListRemoveProduct):
    template_name = 'oscar/customer/wishlists/wishlists_delete_product.html'

class WishListUpdateView(CoreWishListUpdateView):
    template_name = 'oscar/customer/wishlists/wishlists_form.html'