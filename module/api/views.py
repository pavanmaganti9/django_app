from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer


class ListSongsView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'id'
	queryset = Songs.objects.all()
	serializer_class = SongsSerializer
	
class ListSongsView2(generics.ListAPIView):
	queryset = Songs.objects.all()
	serializer_class = SongsSerializer
	
class ListSongsCreateView(generics.CreateAPIView):
	lookup_field = 'id'
	queryset = Songs.objects.all()
	serializer_class = SongsSerializer