from django.forms import ModelForm
from .models import Category

class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']