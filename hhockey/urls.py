"""hhockey URL Configuration
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.contrib.sitemaps.views import sitemap
from hhblog.sitemaps import PostSitemap

from oscar.app import application as oscarApp
from staticContent import views as staticViews

from oscarCustom.customer.views import AccountAuthView
from axes.decorators import watch_login

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', staticViews.home, name='home_page'),
    url(r'shop/password-reset/$', password_reset, {'template_name':'oscar/registration/password_reset_form.html',
                                                   'post_reset_redirect': 'password_reset_done'}, name='password_reset'),
    url(r'shop/password_reset/done/$', password_reset_done, {'template_name':
                                                                 'oscar/registration/password_reset_done.html'},
                                                                 name='password_reset_done'),
    url(r'^shop/password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm,
                                         {'template_name':'oscar/registration/password_reset_confirm.html',
                                          'post_reset_redirect': 'password_reset_complete'},
                                           name='password_reset_confirm'),
    url(r'^shop/password-reset/complete/$', password_reset_complete,
                                         {'template_name':'oscar/registration/password_reset_complete.html'},
                                         name='password_reset_complete'),
    url(r'shop/accounts/login', watch_login(AccountAuthView.as_view())),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^usergt/', include('hhockeyUser.urls', namespace='usergt', app_name='usergt')),
    url(r'shop/', include(oscarApp.urls)),
    url(r'^about/$', staticViews.about, name='about_page'),
    url(r'^warranty/$', staticViews.warranty, name='warranty_page'),
    url(r'^contact/$', staticViews.contact, name='contact_page'),
    url(r'^faq/$', staticViews.faq, name='faq_page'),
    url(r'^terms/$', staticViews.toc, name='toc_page'),
    url(r'^privacy/$', staticViews.privacy, name='privacyPolicy_page'),
    url(r'^sticks/$', staticViews.sticks, name='sticks_page'),
    url(r'^locked/$', staticViews.locked, name='locked_page'),
    url(r'^hhadmin/', admin.site.urls),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^blog/', include('hhblog.urls', namespace='blog', app_name='blog')),
    url(r'^gametime/', include('gametime.urls', namespace='game', app_name='game')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)