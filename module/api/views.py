from django.shortcuts import render
from django.db.models import Q
# Create your views here.
from rest_framework import generics, mixins
from .models import Songs
from .serializers import SongsSerializer


class ListSongsView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'id'
	queryset = Songs.objects.all()
	serializer_class = SongsSerializer
	
class ListSongsView2(mixins.CreateModelMixin, generics.ListAPIView):
	queryset = Songs.objects.all()
	serializer_class = SongsSerializer
	
	def get_queryset(self):
		queryset = Songs.objects.all()
		query = self.request.GET.get("q")
		if query is not None:
			queryset = queryset.filter(Q(title__icontains=query)|Q(artist__icontains=query)).distinct()
			return queryset
	
	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)
	
class ListSongsCreateView(generics.CreateAPIView):
	lookup_field = 'id'
	queryset = Songs.objects.all()
	serializer_class = SongsSerializer