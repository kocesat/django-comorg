from django.urls import path
from . import views

app_name = 'document'

urlpatterns = [
    # document urls
    path('<int:folder_id>/', views.document_list, name='document_list'),
    path('', views.document_list, name='document_list'),
    # folder urls
    path('<int:parent_folder_id>/folder_create/', views.folder_create, name='folder_create'),
    path('folder_create/', views.folder_create, name='folder_create'),
    path('<int:folder_id>/folder_delete/', views.folder_delete, name='folder_delete'),
    path('<int:folder_id>/folder_edit/', views.folder_edit, name='folder_edit'),
    # file urls
    path('<int:parent_folder_id>/file_upload/', views.file_upload, name='file_upload'),
    path('<int:file_id>/file_download/', views.file_download, name='file_download'),
    path('<int:file_id>/file_delete/', views.file_delete, name='file_delete'),
]