from django.contrib import admin
from django.urls import path
from .views import crudlistview, cruddetailview

urlpatterns = [
	path('list', crudlistview.as_view(), name='list'),
	path('detail/<int:pk>', cruddetailview.as_view(), name='detail'),
]