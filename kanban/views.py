from django.http import HttpResponse
from django.template import loader
from django.core import serializers

from .models import Todo, models
from .forms import TodoForm


def get_kanban(request):
    print(request.method)
    if request.method == "POST":
        todo = Todo(text=request.POST['text'], todo_type="todo")
        todo.save()

    todos = Todo.objects.all()
    form = TodoForm()
    context = {
        "todos": serializers.serialize('json', todos),
        "todos1": todos,
        "form": form,
    }

    print(context["todos"], todos)

    template = loader.get_template("kanban.html")
    return HttpResponse(template.render(context, request))
