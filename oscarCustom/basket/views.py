from oscar.apps.basket.views import BasketView as CoreBasketView

import json
from django.http import HttpResponse

from django.template import RequestContext
from django.template.loader import render_to_string


class BasketView(CoreBasketView):
    template_name = 'oscar/basket/basket.html'

    def json_response(self, ctx, flash_messages):
        super(BasketView, self).json_response(ctx, flash_messages)
        basket_html = render_to_string(
            'oscar/basket/partials/basket_content.html',
            RequestContext(self.request, ctx))
        payload = {
            'content_html': basket_html,
            'messages': flash_messages.as_dict()}
        return HttpResponse(json.dumps(payload),
                            content_type="application/json")



