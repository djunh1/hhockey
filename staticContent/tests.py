from django.test import TestCase
from django.core.urlresolvers import resolve
from staticContent import views as staticViews


class ViewStaticPageTests(TestCase):
'''
Tests only the static pages are returning correctly.
'''

    def test_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, staticViews.home)

    def test_about_page(self):
        found = resolve('/about/')
        self.assertEqual(found.func, staticViews.about)

    def test_contact_page(self):
        found = resolve('/contact/')
        self.assertEqual(found.func, staticViews.contact)

    def test_faq_page(self):
        found = resolve('/faq/')
        self.assertEqual(found.func, staticViews.faq)

    def test_terms_page(self):
        found = resolve('/terms/')
        self.assertEqual(found.func, staticViews.toc)

    def test_privacy_page(self):
        found = resolve('/privacy/')
        self.assertEqual(found.func, staticViews.privacy)

