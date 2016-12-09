from django.conf.urls import url

from apps.music.views import DetailView, AlbumCreate, AlbumUpdate, AlbumDelete, UserFormView, SongDetailView, SongCreate, \
    SongUpdate, SongDelete, SongListView
from apps.music.views import index, detail, favorite, IndexView

app_name='music'

urlpatterns=[
    #/music/
    url(r'^$',IndexView.as_view(),name='index'),

    url(r'^register/$',UserFormView.as_view(),name='register'),

    #/music/<pk>/
    url(r'^(?P<pk>[0-9]+)/$',DetailView.as_view(),name='detail'),

    #/music/<album_id>/favorite/
    url(r'^(?P<album_id>[0-9]+)/favorite/$',favorite,name='favorite'),

    #/music/album/add/
    url(r'^album/add/$',AlbumCreate.as_view(),name='album-add'),

    #/music/album/2/
    url(r'^album/(?P<pk>[0-9]+)/$',AlbumUpdate.as_view(),name='album-update'),

    #/music/album/2/delete/
    url(r'^album/(?P<pk>[0-9]+)/delete/$',AlbumDelete.as_view(),name='album-delete'),

    #/music/
    url(r'^song/$',SongListView.as_view(),name='song-list'),

    #music/song/<pk>/
    url(r'^song/(?P<pk>[0-9]+)/$',SongDetailView.as_view(),name='song-detail'),

    #/music/song/add/
    url(r'^song/add/$',SongCreate.as_view(),name='song-add'),

    #music/song/<pk>/edit/
    url(r'^song/(?P<pk>[0-9]+)/edit/$',SongUpdate.as_view(),name='song-update'),

    # /music/song/2/delete/
    url(r'^song/(?P<pk>[0-9]+)/delete/$', SongDelete.as_view(), name='song-delete'),
]