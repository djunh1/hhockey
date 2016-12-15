from oscar.apps.catalogue.reviews.views import CreateProductReview as CoreCreateProductReview
from oscar.apps.catalogue.reviews.views import ProductReviewList as CoreProductReviewList
from oscar.apps.catalogue.reviews.views import ProductReviewDetail as CoreProductReviewDetail


class CreateProductReview(CoreCreateProductReview):
    template_name = "oscar/catalogue/reviews/review_form.html"


class ProductReviewList(CoreProductReviewList):
    template_name = 'oscar/catalogue/reviews/review_list.html'


class ProductReviewDetail(CoreProductReviewDetail):
    template_name = "oscar/catalogue/reviews/review_detail.html"


