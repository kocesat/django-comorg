from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Folder, File
from .forms import CategoryCreateForm
from django.contrib import messages


def index(request):
    categories = Category.objects.all()
    return render(request, 'document/index.html', {'categories': categories})

def category_new(request):
    '''
    Create a new category
    '''
    # TODO: Add permission check or group check (Only SYSTEM_ADMIN and SYSTEM_BUSINESS groups can create a category )
    if request.method == 'POST':
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully')
        else:
            messages.error(request, 'Category cant be created')
        return redirect('document:index')
    else:
        form = CategoryCreateForm()
        return render(request, 'document/category/new.html', {'form': form})


def folder_list(request, category_id: int):
    """List the folder giving a category"""
    category = get_object_or_404(Category, id=category_id)
    folders = category.folders.all()
    return render(request, 'document/folder/list.html', context={'folders': folders, 'category': category})
