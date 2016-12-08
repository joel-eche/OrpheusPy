from django.contrib.auth import authenticate, login
from django.http import HttpResponse,Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from OrpheusPy.forms import UserForm
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

class DetailView(DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model=Album
    fields=['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model=Album
    success_url = reverse_lazy('music:index')

class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'
    #Display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #Process form data
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            #Cleaned(normalized) data
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #Returns User objects if credentials are correct
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music:index')
        return render(request,self.template_name,{'form':form})