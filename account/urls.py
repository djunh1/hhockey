from django.conf.urls import url
from account.views import edit, register, editprofile
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done, \
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete


urlpatterns = [

    url(r'^edit/$', edit, name='edit'),
    url(r'^profile$', editprofile, name='edit_profile'),
    url(r'^register/$', register, name="register"),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout,  name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),

    url(r'^password-change/$', password_change,
        {'template_name': 'registration/password_change_form.html',
         'post_change_redirect': 'account:password_change_done'}
        , name='password_change'),
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),


    url(r'^password-reset/$',
        password_reset,
        {'post_reset_redirect': 'account:password_reset_done'}, name='password_reset'),

    url(r'^password-reset/done/$',
        password_reset_done, name='password_reset_done'),

    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm,
        {'post_reset_redirect': 'account:password_reset_complete'},
        name='password_reset_confirm'),

    url(r'^password-reset/complete/$',
        password_reset_complete,
        name='password_reset_complete'),

]
