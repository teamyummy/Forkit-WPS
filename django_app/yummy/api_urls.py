from django.conf.urls import url
from rest_framework.authtoken import views
from dining import apis as d_apis
from member import apis as m_apis

urlpatterns = [
    url(r'^v1/users/$', m_apis.UserList.as_view(), name='user-list'),
    url(r'^v1/users/(?P<pk>\d+)/$', m_apis.UserDetail.as_view(), name='user-detail'),

    url(r'^v1/restaurants/$',
        d_apis.RestaurantList.as_view(), name='restaurant-list'),
    url(r'^v1/restaurants/(?P<pk>\d+)/$',
        d_apis.RestaurantDetail.as_view(), name='restaurant-detail'),

    url(r'^v1/restaurants/(?P<rest_id>\d+)/menus/$',
        d_apis.MenuList.as_view(), name='menu-list'),
    url(r'^v1/restaurants/(?P<rest_id>\d+)/menus/(?P<pk>\d+)/$',
        d_apis.MenuDetail.as_view(), name='menu-detail'),

    url(r'^v1/restaurants/(?P<rest_id>\d+)/images/$',
        d_apis.RestaurantImgList.as_view(), name='rest-img-list'),
    url(r'^v1/restaurants/(?P<rest_id>\d+)/images/(?P<pk>\d+)/$',
        d_apis.RestaurantImgDetail.as_view(), name='rest-img-detail'),

    url(r'^v1/restaurants/(?P<rest_id>\d+)/reviews/$',
        d_apis.ReviewList.as_view(), name='rest-review-list'),
    url(r'^v1/restaurants/(?P<rest_id>\d+)/reviews/(?P<pk>\d+)/$',
        d_apis.ReviewDetail.as_view(), name='rest-review-detail'),

    url(r'^v1/restaurants/(?P<rest_id>\d+)/tags/$',
        d_apis.TagList.as_view(), name='rest-tag-list'),
    url(r'^v1/restaurants/(?P<rest_id>\d+)/tags/(?P<pk>\d+)/$',
        d_apis.TagDetail.as_view(), name='rest-tag-detail'),

    url(r'^v1/restaurants/(?P<rest_id>\d+)/favors/$',
        d_apis.FavorList.as_view(), name='rest-favor-list'),
    url(r'^v1/restaurants/(?P<rest_id>\d+)/favors/(?P<pk>\d+)/$',
        d_apis.FavorDetail.as_view(), name='rest-favor-detail'),

    url(r'^v1/restaurants/(?P<rest_id>\d+)/reviews/(?P<review_id>\d+)/images/$',
        d_apis.ReviewImgList.as_view(), name='review-img-list'),
    url(r'^v1/restaurants/(?P<rest_id>\d+)/reviews/(?P<review_id>\d+)/images/(?P<pk>\d+)/$',
        d_apis.ReviewImgDetail.as_view(), name='review-img-detail'),

    url(r'^v1/restaurants/(?P<rest_id>\d+)/reviews/(?P<review_id>\d+)/likes/$',
        d_apis.LikeList.as_view(), name='review-like-list'),
    url(r'^v1/restaurants/(?P<rest_id>\d+)/reviews/(?P<review_id>\d+)/likes/(?P<pk>\d+)/$',
        d_apis.LikeDetail.as_view(), name='review-like-detail'),

    url(r'^v1/token-auth/', views.obtain_auth_token),

#    url(r'^v1/menus/$', d_apis.MenuList.as_view(), name='menu-list'),
#    url(r'^v1/menus/(?P<pk>\d+)/$', d_apis.MenuDetail.as_view(), name='menu-detail'),

#    url(r'^v1/reviews/', include('dining.urls.apis')), 
]

