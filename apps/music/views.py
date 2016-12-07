from django.http import HttpResponse,Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import loader
from django.views.generic import DetailView
from django.views.generic import ListView

from apps.music.models import Album,Song

def index(request):
    all_albums=Album.objects.all()
    template=loader.get_template('music/index.html')
    context={
        'all_albums':all_albums
    }
    return HttpResponse(template.render(context,request))
    #or :) :
    #return render(request,'music/index.html',context)

def detail(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    #try:
    #    album=Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Album does not exist")
    return render(request,'music/detail.html',{'album':album})

def favorite(request,album_id):
    album=get_object_or_404(Album,pk=album_id)
    try:
        selected_song=album.song_set.get(pk=request.POST['song'])
    except(KeyError,Song.DoesNotExist):
        return render(request,'music/detail.html',{
            'album':album,
            'error_message':"You did not select a valid song"
        })
    else:
        selected_song.is_favorite=True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})

class IndexView(ListView):
    model = Album
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()

class DetailView(DetailView):
    model = Album
    template_name = 'music/detail.html'