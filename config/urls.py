from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from CacheDemo import urls as cache_demo_urls

urlpatterns = [
    url(r'', include('CacheDemo.urls', namespace='main', app_name='CacheDemo')),
    url(r'^admin/', admin.site.urls),
]
