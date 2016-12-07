from django.conf.urls import url

from apps.music.views import DetailView
from apps.music.views import index, detail, favorite, IndexView

app_name='music'

urlpatterns=[
    #/music/
    url(r'^$',IndexView.as_view(),name='index'),

    #/music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$',DetailView.as_view(),name='detail'),

    #/music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$',favorite,name='favorite'),
]