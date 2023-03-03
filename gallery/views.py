from django.shortcuts import render
from .models import Album, Photo, Comment


# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, "gallery/album_list.html")

def album(request, album_id):
    return HttpResponse("Showing album %s" % album_id)

def photo(request, album_id, photo_id):
    return HttpResponse("Showing photo %s from album %s" % (photo_id, album_id))