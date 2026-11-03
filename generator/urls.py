from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name= 'home'),
    path('username/', views.generate_username , name='username'),
    path('password/', views.generate_password , name='password')
]