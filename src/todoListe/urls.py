from django.urls import path, include
from .views import CreateTodo, ListeTodo, DeleteTodo, UpdateTodo, DetailTodo

urlpatterns = [
    path('create/', CreateTodo.as_view(), name='create-todo'),
    path('todo-list/', ListeTodo.as_view(), name='todo-liste'),
    path('<str:slug>/delete/', DeleteTodo.as_view(), name='delete-todo'),
    path('<str:slug>/update/', UpdateTodo.as_view(), name='update-todo'),
    path('<str:slug>/detail/', DetailTodo.as_view(), name='detail-todo')
]