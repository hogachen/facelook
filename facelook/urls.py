from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^get_user/(?P<user_id>.*)/$', views.get_user, name='get_user'),
    url(r'^get_newest_image/(?P<user_id>.*)/(?P<select_date>.*)/(?P<select_page>.*)/$', views.get_newest_image, name='get_newest_image'),
    url(r'^register/(?P<user_name>.*)/(?P<email>.*)/(?P<tel>.*)/(?P<password>.*)/$', views.register, name='register'),
    url(r'^login/(?P<email>.*)/(?P<password>.*)/$', views.login, name='register'),
    url(r'^get_user_collect_list/(?P<user_id>.*)/$', views.get_user_collect_list, name='get_user_collect_list'),
    url(r'^insert_faviour/(?P<user_id>.*)/(?P<image_id>.*)/$', views.insert_faviour, name='insert_faviour'),
    url(r'^insert_collect/(?P<user_id>.*)/(?P<image_id>.*)/$', views.insert_collect, name='insert_collect'),
]
