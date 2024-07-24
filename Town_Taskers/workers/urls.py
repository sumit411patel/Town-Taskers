"""hifixsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from workers import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),

    path('worker_register', views.worker_register, name='worker_register'),
    path('worker_store', views.worker_store, name='worker_store'),   
    path('worker_edit_profile', views.worker_edit_profile, name='worker_edit_profile'),
    path('worker_update/<int:id>', views.worker_update, name='worker_update'),

    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),

    path('contact', views.contact, name='contact'),
    path('contact_store', views.contact_store, name='contact_store'),

    path('user_request', views.user_request, name='user_request'),
    path('view_user_request/<int:id>', views.view_user_request, name='view_user_request'),
     

    path('apply_request/<int:id>', views.apply_request, name='apply_request'),
    path('apply_request_store/<int:id>', views.apply_request_store, name='apply_request_store'),
]
