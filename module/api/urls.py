from django.contrib import admin
from django.urls import path, re_path, include


from .views import ListSongsView, ListSongsView2, ListSongsCreateView


urlpatterns = [
    path('songs/', ListSongsView2.as_view(), name="songs-all"),
	re_path('songs/(?P<id>\d+)$', ListSongsView.as_view(), name="songs-all"),
	re_path('songs/create', ListSongsCreateView.as_view(), name="songs-all"),
]
