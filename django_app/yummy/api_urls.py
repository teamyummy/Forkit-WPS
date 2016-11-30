from django.conf.urls import url
from dining import apis as d_apis
from member import apis as m_apis

urlpatterns = [
    url(r'^v1/users/$', m_apis.UserList.as_view(), name='user-list'),
    url(r'^v1/users/(?P<pk>\d+)/$', m_apis.UserDetail.as_view(), name='user-detail'),

    url(r'^v1/restaurants/$',
        d_apis.RestaurantList.as_view(), name='restaurant-list'),
    url(r'^v1/restaurants/(?P<pk>\d+)/$',
        d_apis.RestaurantDetail.as_view(), name='restaurant-detail'),
    url(r'^v1/restaurants/(?P<pk>\d+)/menus/$',
        d_apis.MenuList.as_view(), name='menu-list'),

    url(r'^v1/menus/$', d_apis.MenuList.as_view(), name='menu-list'),
    url(r'^v1/menus/(?P<pk>\d+)/$', d_apis.MenuDetail.as_view(), name='menu-detail'),

#    url(r'^v1/reviews/', include('dining.urls.apis')), 
]

