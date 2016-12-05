from django.conf.urls import url
from . import views

app_name = 'dining'

urlpatterns = [
    url(r'^restaurant/$', views.restaurant_list, name='restaurant-list'),
    url(r'^restaurant/new/$', views.restaurant_new, name='restaurant-new'),
    url(r'^restaurant/detail/(?P<pk>\d+)/$',
                            views.restaurant_detail, name='restaurant-detail'),
    url(r'^restaurant/update/(?P<pk>\d+)/$',
                            views.restaurant_update, name='restaurant-update'),
    url(r'^restaurant/delete/(?P<pk>\d+)/$',
                            views.restaurant_delete, name='restaurant-delete'),
]

