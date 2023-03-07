from django.shortcuts import render, get_object_or_404
from .models import Album, Photo, Comment
from django.http import Http404
from django.http import HttpResponse


def index(request):
    album_list = Album.objects.all()
    return render(request, "gallery/album_list.html", {"album_list": album_list})

def album(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    photos = album.photo_set.all()
    return render(request, "gallery/album.html", {"album": album, "photos": photos, "photos_count": photos.count()})

def photo(request, album_id, photo_id):
    return HttpResponse("Showing photo %s from album %s" % (photo_id, album_id))