from django.conf import settings
from django.shortcuts import render
from .models import Song
from .forms import SongUpload
from django.db.models import Q
# Create your views here.

def handle_uploaded_image(f):  
    with open('static/media/covers/'+str(f.name), 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk) 
def handle_uploaded_mp3(f):  
    with open('static/media/songs/'+str(f.name), 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)    

def upload_song(request):
    if request.method == "POST":
        form =SongUpload(request.POST,request.FILES)
        if form.is_valid():
            handle_uploaded_image(request.FILES["song_image"])
            handle_uploaded_mp3(request.FILES["song_file"])
            form.save()
    else:
        form = SongUpload()
    return render(request, "songs/songs_upload.html",{"form":form})

def search_song(request):
    return render(request,"songs/songs_search.html")

def all_songs(request):
    songs = Song.objects.all()
    return render(request,'songs/search_results.html', {"songs": songs})

def search_results(request):
    query = request.GET.get('q')
   
    try:
        query = str(query)
        if query=='':
            return render(request,'songs/search_results.html', {"songs": None})
    except ValueError:
        query = None
        songs = None
    if query:
        if Song.objects.filter(Q(name__contains=query) | Q(singer__contains=query)).exists():
            songs = Song.objects.filter(Q(name__contains=query) | Q(singer__contains=query))
        else :
            songs = None
    return render(request,'songs/search_results.html', {"songs": songs})


def play_song(request,song_id):
    song = Song.objects.filter(id=song_id).first()
    #path = settings.MEDIA_ROOT
    image_path = '/'.join(song.song_image.path.split('\\'))
    file_path = '/'.join(song.song_file.path.split('\\'))
    return render(request, "songs/player.html",{"name": song.name, "image": image_path, "singer": song.singer, "file":file_path})
