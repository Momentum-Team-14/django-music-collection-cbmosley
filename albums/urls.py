from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_albums, name='list_albums'),
    path('albums/<int:pk>', views.album_detail, name='album_detail'),
    path('albums/new/', views.create_album, name='create_album'),
    path('albums/<int:pk>/edit/', views.albums_edit, name='albums_edit'),
    path('delete_album/<int:pk>', views.delete_album, name="delete_album")
]
