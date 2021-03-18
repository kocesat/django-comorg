from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'account'

urlpatterns = [
    path('', views.account_list, name='account_list'),
    path('participants/', views.participant_list, name='participant_list'),
    path('<int:user_id>/activate/', views.activate_user, name='activate_user'),
    path('<int:user_id>/deactivate/', views.deactivate_user, name='deactivate_user'),
    path('register/', views.register, name='register'),

    # auth views
    path('login/', auth_views.LoginView.as_view, name='login'),
]