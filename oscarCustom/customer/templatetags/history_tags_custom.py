from django import template
from django.core.urlresolvers import Resolver404, resolve
from django.utils import six
from django.utils.six.moves.urllib import parse
from django.utils.translation import ugettext_lazy as _

from oscar.apps.customer import history
from oscar.core.loading import get_model

Site = get_model('sites', 'Site')

register = template.Library()


@register.inclusion_tag('oscar/customer/history/recently_viewed_products.html',
                        takes_context=True)
def recently_viewed_products(context, current_product=None):
    """
    Inclusion tag listing the most recently viewed products
    """
    request = context['request']
    products = history.get(request)
    if current_product:
        products = [p for p in products if p != current_product]
    return {'products': products,
            'request': request}
