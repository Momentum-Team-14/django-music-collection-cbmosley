from django.shortcuts import render, get_object_or_404, redirect
from .models import Album
from .forms import AlbumForm
# Create your views here.


def list_albums(request):
    albums = Album.objects.all()
    return render(request, 'albums/album_home.html', {"albums": albums})


def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/album_detail.html", {"album": album})


def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('list_albums')
    else:
        form = AlbumForm()
    return render(request, 'albums/create_album.html', {'form': form})


def albums_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('album_detail', pk=album.pk)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'albums/create_album.html', {'form': form})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return render(request, 'albums/album_home.html', {"album": album})
