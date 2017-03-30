from oscar.apps.catalogue.views import CatalogueView as CoreCatalogueView
from oscar.apps.catalogue.views import ProductCategoryView as CoreProductCategoryView
from oscar.apps.catalogue.views import ProductDetailView as CoreProductDetailView


class CatalogueView(CoreCatalogueView):
    template_name = 'oscar/catalogue/browse.html'


class ProductCategoryView(CoreProductCategoryView):
    template_name = 'oscar/catalogue/category.html'


class ProductDetailView(CoreProductDetailView):
    template_folder = "oscar/catalogue"

    def get_template_names(self):
        super(ProductDetailView, self).get_template_names()
        if self.template_name:
            return [self.template_name]

        return [
            '%s/detail-for-upc-%s.html' % (
                self.template_folder, self.object.upc),
            '%s/detail-for-class-%s.html' % (
                self.template_folder, self.object.get_product_class().slug),
            '%s/detail.html' % (self.template_folder)]



