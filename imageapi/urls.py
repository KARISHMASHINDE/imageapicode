from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from imageapi import views

urlpatterns = [
    path('user/', views.userList.as_view()),
    path('userpost/', views.userpost.as_view()),
    path('user_details/<int:pk>/', views.userDetail.as_view()),
    path('profile/', views.profileList.as_view()),
    path('profilepost/', views.profilepost.as_view()),
    path('profile_details/<int:pk>/', views.profileDetail.as_view())
]