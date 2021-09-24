from django.urls import path
from . import views

app_name = 'document'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.category_new, name='category_new'),
    path('<int:category_id>/folders/', views.folder_list, name='folder_list'),
]