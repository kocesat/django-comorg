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
    path('<int:user_id>/role_assing/', views.role_assing, name='role_assing'),

    # auth views
    path('login/', auth_views.LoginView.as_view(template_name='account/users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/users/logout.html'), name='logout'),
]