from django.urls import path
from . import views

app_name = 'document'

urlpatterns = [
    path('<int:folder_id>/', views.document_list, name='document_list'),
    path('', views.document_list, name='document_list'),
    path('<int:parent_folder_id>/folder_create/', views.folder_create, name='folder_create'),
    path('folder_create/', views.folder_create, name='folder_create'),
    path('<int:parent_folder_id>/file_upload/', views.file_upload, name='file_upload'),
    path('<int:file_id>/file_download/', views.file_download, name='file_download'),
    path('<int:folder_id>/folder_delete/', views.folder_delete, name='folder_delete'),
    path('<int:file_id>/file_delete/', views.file_delete, name='file_delete'),
]