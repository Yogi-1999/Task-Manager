from django import forms
from dolist.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model= Task
        fields= ['task','done']