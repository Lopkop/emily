from django.urls import path
from .views import get_kanban

urlpatterns = [
    path("", get_kanban, name="get_kanban"), # todo: finish
]

