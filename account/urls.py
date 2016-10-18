from django.conf.urls import url
from account import views

urlpatterns = [

    url(r'^edit/$', views.edit, name='edit'),
    url(r'^register/$', views.register, name="register"),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',  name='logout'),
    url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^password-change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'registration/password_change_form.html', 'post_change_redirect': 'account:password_change_done'}
        , name='password_change'),
    url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),


    url(r'^password-reset/$',
        'django.contrib.auth.views.password_reset',
        {'post_reset_redirect': 'account:password_reset_done'},
        name='password_reset'),

    url(r'^password-reset/done/$',
        'django.contrib.auth.views.password_reset_done',
        name='password_reset_done'),

    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        'django.contrib.auth.views.password_reset_confirm',
        name='password_reset_confirm'),

    url(r'^password-reset/complete/$',
        'django.contrib.auth.views.password_reset_complete',
        name='password_reset_complete'),

]
