from django.test import TestCase
from django.core.urlresolvers import resolve
import staticContent.views as staticViews


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
        request = self.client.get('/about/')
        self.assertTemplateUsed(request, 'site/about.html')

    def test_contact_page(self):
        found = resolve('/contact/')
        self.assertEqual(found.func, staticViews.contact)
        request = self.client.get('/contact/')
        self.assertTemplateUsed(request, 'site/contact.html')

    def test_faq_page(self):
        found = resolve('/faq/')
        self.assertEqual(found.func, staticViews.faq)
        request = self.client.get('/faq/')
        self.assertTemplateUsed(request, 'site/freqQuest.html')

    def test_terms_page(self):
        found = resolve('/terms/')
        self.assertEqual(found.func, staticViews.toc)
        request = self.client.get('/terms/')
        self.assertTemplateUsed(request, 'site/toc.html')

    def test_privacy_page(self):
        found = resolve('/privacy/')
        self.assertEqual(found.func, staticViews.privacy)
        request = self.client.get('/privacy/')
        self.assertTemplateUsed(request, 'site/privacyPolicy.html')




