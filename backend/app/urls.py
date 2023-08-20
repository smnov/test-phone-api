from django.urls import path
from . import views

urlpatterns = [
    path('send_auth_code/', views.SendAuthCode.as_view()),
    path('check_auth_code/', views.CheckAuthCode.as_view()),
    path('invited_users/', views.InvitedUsersView.as_view()),
    path('profile/', views.UserProfileView.as_view()),
]