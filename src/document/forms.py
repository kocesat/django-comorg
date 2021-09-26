from django import forms
from .models import Category, Folder

class CategoryCreateForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['name']

class FolderCreateForm(forms.ModelForm):
    
    class Meta:
        model = Folder
        fields = ['name']
