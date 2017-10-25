from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'signup/$', views.signup, name='signup'),
    url(r'login/$', views.login_user, name='login'),
    url(r'signout/$', views.signout, name='signout'),
    url(r'signup_success/$', views.signup_success, name='signup_success'),
]
