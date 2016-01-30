from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

# def root_view(request):
#     return redirect('blog.views.index')

#1.9.1


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^blog/' , include('blog.urls')),  #blog의 urls.py를 include해라
    # url(r'^$',views.index) #'blog.views.index'
    url(r'^$', lambda request: redirect('blog.views.index')),
    # url(r'^$', root_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
