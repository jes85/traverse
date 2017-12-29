from django.conf.urls import url

from . import views

app_name = 'activitysearch'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/', views.detail, name='detail'),
    url(r'^home/', views.home, name='detail'),
    url(r'^search/', views.search, name='detail'),
]
