from oscar.apps.basket.views import BasketView as CoreBasketView


class BasketView(CoreBasketView):
    template_name = 'oscar/basket/basket.html'

