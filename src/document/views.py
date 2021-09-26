from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Folder, File
from .forms import CategoryCreateForm, FolderCreateForm
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


def folder_new(request, category_id: int, parent_folder_id: int = None):
    if request.method == 'GET':
        form = FolderCreateForm()
        return render(request, 'document/folderfile/newfolder.html', {'form': form, 'category_id': category_id, 'parent_folder_id': parent_folder_id})
    else:
        form = FolderCreateForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            category = get_object_or_404(Category, id=category_id)
            folder.category = category
            if parent_folder_id:
                parent_folder = get_object_or_404(Folder, id=parent_folder_id)
                folder.parent = parent_folder
                folder.save()
                return redirect('document:document_list', category_id=category.id, folder_id=parent_folder.id)
            folder.save()
            return redirect('document:document_list', category_id=category.id)


def document_list(request, category_id: int, folder_id: int = None):
    """List the folders or files giving a folder_id or category_id"""
    if folder_id:
        parent_folder = get_object_or_404(Folder, id=folder_id)
        folders = parent_folder.subfolders.all()
        files = parent_folder.files.all()
        return render(request, 'document/folderfile/list.html', {'folders': folders, 'files': files, 'parent_folder': parent_folder} )
    category = get_object_or_404(Category, id=category_id )
    folders = category.folders.filter(parent=None)
    return render(request, 'document/folderfile/list.html', {'folders': folders, 'category': category} )
