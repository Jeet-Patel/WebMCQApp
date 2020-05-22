from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    url( r'^login/$',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    url(r'^logout/$', auth_views.LogoutView, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]