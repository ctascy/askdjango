from django.conf.urls import url, include


#1.9.1
from blog import views

urlpatterns = [
    #url(r'^$' , include('blog.urls'))
    url(r'^$', views.index), #'blog.views.index'
    url(r'^posts/$' , views.post_list),
    url(r'^posts/(?P<pk>\d+)/$', views.post_detail),
    url(r'^posts/(?P<post_pk>\d+)/comments/new/$', views.comment_new),
]
