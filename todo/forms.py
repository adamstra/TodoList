from django import forms
from django.forms import ModelForm

from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
    
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Nouvelle tache ....",
            })
    )