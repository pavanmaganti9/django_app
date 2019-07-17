from django import forms
from .models import crud

class crudcreate(forms.ModelForm):
	class Meta:
		model = crud
		fields = [
			'name', 'email', 'content', 'gender'
		]