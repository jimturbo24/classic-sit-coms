from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="show-index" ),
    url(r'^(?P<show_id>[0-9]+)/$', views.view_show, name='content-view_show')
]
