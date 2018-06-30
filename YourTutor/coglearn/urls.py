from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/',views.dashboard, name='dashboard'),
    url(r'^login/$', auth_views.login,{'template_name': 'index.html'}, name='login'),
    url(r'^logout/',auth_views.logout,name='logout'),

]