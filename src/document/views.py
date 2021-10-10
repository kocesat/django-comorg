from django.shortcuts import render, redirect, get_object_or_404
from .models import Folder, File
from .forms import (FolderCreateForm,
                    FileUploadForm, FolderEditForm)
from django.contrib import messages
from django.http import FileResponse


def document_list(request, folder_id: int=None):
    parent_folder = None
    if folder_id:
        parent_folder = get_object_or_404(Folder, id=folder_id)
        folders = parent_folder.subfolders.all()
        files = parent_folder.files.all()
    else:
        folders = Folder.objects.filter(parent=None)
        files = None
    return render(request, 'document/document_list.html', {
        'folders': folders,
        'files': files,
        'parent_folder': parent_folder
    })
    

def folder_create(request, parent_folder_id: int=None):
    if request.method == 'GET':
        form = FolderCreateForm()
        return render(request, 'document/folder/create.html', {'form': form, 'parent_folder_id': parent_folder_id})
    else:
        form = FolderCreateForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            if parent_folder_id:
                parent_folder = get_object_or_404(Folder, id=parent_folder_id)
                folder.parent = parent_folder
                folder.save()
                return redirect('document:document_list', folder_id=parent_folder_id )
            folder.save()
            return redirect('document:document_list')


def file_upload(request, parent_folder_id: int):
    parent_folder = get_object_or_404(Folder, id=parent_folder_id)
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_obj = form.save(commit=False)
            file_obj.parent_folder = parent_folder
            file_obj.save()
            return redirect('document:document_list', folder_id=parent_folder.id)
    else:
        form = FileUploadForm()
    return render(request, 'document/file/upload.html', {'form': form, 'parent_folder_id': parent_folder_id})


def file_download(request, file_id: int):
    file_obj = get_object_or_404(File, pk=file_id)
    filename = file_obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response


def folder_delete(request, folder_id: int):
    folder = get_object_or_404(Folder, pk=folder_id)
    parent_folder = folder.parent
    folder.delete()
    messages.success(request, 'Folder deleted successfully')
    if parent_folder:
        return redirect('document:document_list', folder_id=parent_folder.id)
    else:
        return redirect('document:document_list')


def folder_edit(request, folder_id: int):
    folder = get_object_or_404(Folder, pk=folder_id)
    parent_folder = folder.parent
    if request.method == 'POST':
        form = FolderEditForm(instance=folder, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Folder updated successfully.')
            if parent_folder:
                return redirect('document:document_list', folder_id=parent_folder.id)
            else:
                return redirect('document:document_list')
        else:
            messages.error(request, 'Something went wrong')
    else:
        form = FolderEditForm(instance=folder)
    return render(request, 'document/folder/edit.html', {'form': form})


def file_delete(request, file_id: int):
    file_obj = get_object_or_404(File, pk=file_id)
    parent_folder = file_obj.parent_folder
    file_obj.delete()
    messages.success(request, 'File deleted successfully')
    return redirect('document:document_list', folder_id=parent_folder.id)