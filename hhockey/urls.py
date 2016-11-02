"""hhockey URL Configuration


"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from oscar.app import application as oscarApp
from staticContent import views as staticViews


urlpatterns = [
    url(r'^$', staticViews.home, name='home_page'),
    url(r'^about/$', staticViews.about, name='about_page'),
    url(r'^contact/$', staticViews.contact, name='contact_page'),
    url(r'^faq/$', staticViews.faq, name='faq_page'),
    url(r'^terms/$', staticViews.toc, name='toc_page'),
    url(r'^privacy/$', staticViews.privacy, name='privacyPolicy_page'),
    url(r'account/',  include('account.urls', namespace='account')),
    url(r'accounts/', include('allauth.urls')),
    url(r'^shop/', include(oscarApp.urls)),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)