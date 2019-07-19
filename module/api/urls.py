from django.contrib import admin
from django.urls import path, re_path, include


from .views import ListSongsView


urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all")
]
