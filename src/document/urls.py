from django.urls import path
from . import views

app_name = 'document'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.category_new, name='category_new'),
    path('<int:category_id>/folders-files/', views.document_list, name='document_list'),
    path('<int:category_id>/<int:folder_id>/folders-files/', views.document_list, name='document_list'),
    path('<int:category_id>/folder_new', views.folder_new, name='folder_new' ),
    path('<int:category_id>/<int:parent_folder_id>/folder_new', views.folder_new, name='folder_new' ),
]