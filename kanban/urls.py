from django.urls import path
from .views import get_kanban, update_todo_type, update_todo_text, delete_todo_task

urlpatterns = [
    path("", get_kanban, name="get_kanban"),
    path('update_todo_type/', update_todo_type, name='update_todo_type'),
    path('update_todo_text/', update_todo_text, name='update_todo_text'),
    path('delete_todo_task/', delete_todo_task, name='delete_todo_task'),
]
