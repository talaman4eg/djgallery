from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:album_id>', views.album, name='album'),
    path('<int:album_id>/photo/<int:photo_id>', views.photo, name='photo'),
]