from django import forms
from django.forms import ModelForm

from .models import *



class TasksForm(ModelForm):


    class Meta:
        model = Tasks
        fields = ['title', 'complete']




