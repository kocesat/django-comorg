from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.account_list, name='account_list'),
    path('participants/', views.participant_list, name='participant_list'),
]