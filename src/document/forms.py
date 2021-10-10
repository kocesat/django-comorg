from django import forms
from .models import Folder, File


class FolderCreateForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name']


class FolderEditForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ('name', )


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'description', 'is_draft', 'file']