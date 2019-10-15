# coding=utf-8
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('logout/', views.my_logout, name='logout'),
    path('file_upload/', views.model_form_upload, name='file_upload'),
    path('success_upload/', views.SuccessView.as_view(), name='success_upload'),
]