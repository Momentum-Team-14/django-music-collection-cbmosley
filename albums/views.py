from django.shortcuts import render
from .models import Album
# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_home.html', {"albums": albums})
