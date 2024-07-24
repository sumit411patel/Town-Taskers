"""Town_Taskers URL Configuration

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
from myadmin import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),

    # Category

    path('add_category', views.add_category, name='add_category'),
    path('add_category_store', views.add_category_store, name='add_category_store'),
    path('all_categories', views.all_categories, name='all_categories'),
    path('delete_category/<int:id>', views.delete_category, name='delete_category'),
    path('edit_category/<int:id>', views.edit_category, name='edit_category'),
    path('update_category/<int:id>', views.update_category, name='update_category'),

    # Sub_category

    path('add_sub_category', views.add_sub_category, name='add_sub_category'),
    path('add_sub_category_store', views.add_sub_category_store, name='add_sub_category_store'),
    path('all_sub_categories', views.all_sub_categories, name='all_sub_categories'),
    path('delete_sub_category/<int:id>', views.delete_sub_category, name='delete_sub_category'),
    path('edit_sub_category/<int:id>', views.edit_sub_category, name='edit_sub_category'),
    path('update_sub_category/<int:id>', views.update_sub_category, name='update_sub_category'),

    # User

    path('all_users', views.all_users, name='all_users'),
    path('view_all_users/<int:id>', views.view_all_users, name='view_all_users'),
    
    # Worker

    path('all_workers', views.all_workers, name='all_workers'),
    path('view_all_workers/<int:id>', views.view_all_workers, name='view_all_workers'),

    # City

    path('add_city', views.add_city, name='add_city'),
    path('add_city_store', views.add_city_store, name='add_city_store'),
    path('all_cities', views.all_cities, name='all_cities'),
    path('delete_city/<int:id>', views.delete_city, name='delete_city'),
    path('edit_city/<int:id>', views.edit_city, name='edit_city'),
    path('update_city/<int:id>', views.update_city, name='update_city'),

    # Area

    path('add_area', views.add_area, name='add_area'),
    path('add_area_store', views.add_area_store, name='add_area_store'),
    path('all_areas', views.all_areas, name='all_areas'),
    path('delete_area/<int:id>', views.delete_area, name='delete_area'),
    path('edit_area/<int:id>', views.edit_area, name='edit_area'),
    path('update_area/<int:id>', views.update_area, name='update_area'),

    path('feedback', views.feedback, name='feedback'),
    path('inquiry', views.inquiry, name='inquiry'),
    
    path('', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),

    # Report 

    path('user_report', views.user_report, name='user_report'),

    path('user_pdf', views.GeneratePdf.as_view()),

    path('worker_report', views.worker_report, name='worker_report'),

    path('worker_pdf', views.GenerateWorkerPdf.as_view()),

    path('feed_report', views.feed_report, name='feed_report'),

    path('feedback_pdf', views.GenerateFeedbackPdf.as_view()),

    # Worker Authentication

    path('worker_status_approve/<int:id>', views.worker_status_approve, name='worker_status_approve'),
    path('worker_status_reject/<int:id>', views.worker_status_reject, name='worker_status_reject'),
]
