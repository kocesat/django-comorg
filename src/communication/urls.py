from django.urls import path
from . import views

app_name = 'communication'

urlpatterns = [
    path('', views.index, name='broadcast_list'),
    path('unpublished/', views.list_unpublished, name='list_unpublished'),
    path('new/', views.new_broadcast, name='new_broadcast'),
    path('<int:broadcast_id>/publish/', views.publish, name='publish'),
    path('<int:broadcast_id>/unpublish/', views.unpublish, name='unpublish'),
]