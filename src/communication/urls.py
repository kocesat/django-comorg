from django.urls import path
from . import views

app_name = 'communication'

urlpatterns = [
    path('', views.index, name='broadcast_list'),
    path('new/', views.new_broadcast, name='new_broadcast'),
]