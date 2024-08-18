from django.http import HttpResponse
from django.template import loader

from .models import Todo, models
from .forms import TodoForm


def get_kanban(request):
    print(request.method)
    if request.method == "POST":
        print("AAAA", request.POST)

    todos = Todo.objects.all()
    form = TodoForm()
    context = {
        "todos": todos,
        "form": form,
    }

    template = loader.get_template("kanban.html")
    return HttpResponse(template.render(context, request))
