from django.conf.urls import url
from .views import IndexView, CachedView

urlpatterns = [
    url(
        regex=r'^$',
        view=IndexView.as_view(),
        name='index'
    ),
    url(
        regex=r'^cached/$',
        view=CachedView.as_view(),
        name='index'
    )
]
