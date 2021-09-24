from django.shortcuts import render
from document.models import Category

def home(request):
    categories = Category.objects.all()
    return render(request, 'core/base.html', {'categories': categories})