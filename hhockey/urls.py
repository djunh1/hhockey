"""hhockey URL Configuration
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

from oscar.app import application as oscarApp
from staticContent import views as staticViews



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
    url(r'^accounts/', include('allauth.urls')),
    url(r'shop/', include(oscarApp.urls)),
    url(r'^about/$', staticViews.about, name='about_page'),
    url(r'^contact/$', staticViews.contact, name='contact_page'),
    url(r'^faq/$', staticViews.faq, name='faq_page'),
    url(r'^terms/$', staticViews.toc, name='toc_page'),
    url(r'^plans/$', staticViews.plans, name='plans_page'),
    url(r'^privacy/$', staticViews.privacy, name='privacyPolicy_page'),
    url(r'^sticks/$', staticViews.sticks, name='sticks_page'),

    #STRIPE


    #admin
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)