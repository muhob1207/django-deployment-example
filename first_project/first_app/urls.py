from django.contrib import admin
from django.urls import path, include
from first_app import views

app_name = 'first_app'

'''urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other')
]'''
urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/',views.user_login, name='user_login')
]