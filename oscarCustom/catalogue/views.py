from oscar.apps.catalogue.views import CatalogueView as CoreCatalogueView
from oscar.apps.catalogue.views import ProductCategoryView as CoreProductCategoryView
from oscar.apps.catalogue.views import ProductDetailView as CoreProductDetailView


class CatalogueView(CoreCatalogueView):
    template_name = 'oscar/catalogue/browse.html'


class ProductCategoryView(CoreProductCategoryView):
    template_name = 'oscar/catalogue/category.html'


class ProductDetailView(CoreProductDetailView):
    template_folder = "oscar/catalogue"




