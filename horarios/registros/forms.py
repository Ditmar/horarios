from django.forms import ModelForm
from django import forms
from .models import *
class buscarDocenteForm(forms.Form):
	buscar_docente=forms.CharField(max_length=200)
	buscar_docente.widget.attrs={'class': 'form-control',"placeholder":"Buscar Docente"}
class i_j(forms.Form):
	i=forms.CharField(max_length=200)
	j=forms.CharField(max_length=200)
class Filter(forms.Form):
	code=forms.CharField(max_length=100)