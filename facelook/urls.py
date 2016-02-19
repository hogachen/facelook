from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_desc/$', views.user_desc, name='user_desc'),
    url(r'^user_desc/(?P<user_name>.*)/$', views.user_desc_detail, name='user_desc_detail'),
    url(r'^(?P<question_id>[0-9]+)/$',views.results,name='detail'),
]

