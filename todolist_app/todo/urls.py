# todo/urls.py
from django.urls import path
from .views import todo_list , add_todo , edit_todo , delete_todo
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index,name='index'),
    path('', todo_list, name='todo_list'),
    path('add/', add_todo, name='add_todo'),
    path('edit/', edit_todo, name='edit_todo'),
    path('delete/', delete_todo, name='delete_todo'),
]
