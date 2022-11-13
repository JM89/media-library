from django.shortcuts import render, get_object_or_404, redirect

from albums.forms import AlbumForm
from albums.models import Album


def view_album(request, id):
    album = get_object_or_404(Album, pk=id)
    return render(request, "albums/view_album.html", {"album": album})


def list_albums(request):
    return render(request, "albums/list_albums.html", {"albums": Album.objects.all()})


def create_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_albums")
    else:
        form = AlbumForm()
    return render(request, "albums/new_album.html", {"form": form})
