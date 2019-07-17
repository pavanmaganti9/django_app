from django.shortcuts import render
from .models import crud
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,redirect
import datetime
from django.views.generic import DetailView, ListView, UpdateView

from .forms import crudcreate
from django.shortcuts import get_list_or_404, get_object_or_404

def home(request):
	return render(request, 'default.html', {'title': 'Home'})

class crudlistview(ListView):
	model = crud
	template_name = 'crud_list.html'
	context_object_name = 'crud_list'
	
	def queryset(self):
		return crud.objects.all()
	
	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		context['date'] = datetime.datetime.now
		return context
		
class cruddetailview(DetailView):
	model = crud
	template_name = 'crud_detail.html'
	
	
def post_update_new(request, id):
	post = get_object_or_404(crud, id=id)
	form = crudcreate(instance = post)
	if request.method == 'POST':
		form = crudcreate(request.POST)
		post = get_object_or_404(crud, id=id)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			
			post.name = name
			
			post.save()
	
	return render(request, 'update.html', {'form': form})
