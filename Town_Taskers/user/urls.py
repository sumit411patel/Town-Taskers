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
from user import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),

    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),

    path('search_worker', views.search_worker, name='search_worker'),
    path('view_worker_details/<int:id>', views.view_worker_details, name='view_worker_details'),

    path('all_electricians', views.all_electricians, name='all_electricians'),
    path('all_plumbers', views.all_plumbers, name='all_plumbers'),
    path('all_carpenters', views.all_carpenters, name='all_carpenters'),
    path('all_painters', views.all_painters, name='all_painters'),
    

    path('user_register', views.user_register, name='user_register'),
    path('user_store', views.user_store, name='user_store'),
    path('user_edit_profile', views.user_edit_profile, name='user_edit_profile'),
    path('user_update/<int:id>', views.user_update, name='user_update'),

    path('changepass', views.changepass, name='changepass'),
    path('changepass_update', views.changepass_update, name='changepass_update'),

    path('feedback', views.feedback, name='feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'),

    path('contact', views.contact, name='contact'),
    path('contact_store', views.contact_store, name='contact_store'),

    path('post_problem', views.post_problem, name='post_problem'),
    path('post_problem_store', views.post_problem_store, name='post_problem_store'),
    path('view_my_request/<int:id>', views.view_my_request, name='view_my_request'),
    path('all_requests', views.all_requests, name='all_requests'),
    path('post_problem_delete/<int:id>', views.post_problem_delete, name='post_problem_delete'),
    path('request_edit/<int:id>', views.request_edit, name='request_edit'),
    path('request_update/<int:id>', views.request_update, name='request_update'),

    path('applications/<int:id>', views.applications, name='applications'),
    path('applications_delete/<int:id>', views.applications_delete, name='applications_delete'),

    path('hire/<int:id>/<int:worker_id>', views.hire, name='hire'),
    path('hire_store', views.hire_store, name='hire_store'),

    path('history', views.history, name='history'),
    path('get_subcategories_by_id', views.get_subcategories_by_id, name='get_subcategories_by_id'),
]
