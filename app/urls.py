# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('add-todo/', views.add_todo, name='add_todo'),
    path('add-task/', views.add_task, name='add_task'),
    path('add-grade/', views.add_grade, name='add_grade'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontend_page, name='frontend'),
]
