from django.urls import path
from . import views

urlpatterns = [

    path('add_todo/', views.AddToDo, name='add_todo'),
    path('view_todo/', views.ViewTodo, name='view_todo'),
    path('edit_todo/<todo_id>', views.EditTodo, name='edit_todo'),
    path('completed_todo/<todo_id>', views.CompleteTodo, name='complete_todo'),
    path('get_todo_by_status/', views.SearchTodo, name='get_todo_by_status'),
    path('demo/', views.Demo, name='demo'),

]
