from django.http import HttpResponse, JsonResponse
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

    template = loader.get_template("kanban.html")
    return HttpResponse(template.render(context, request))


def update_todo_type(request):
    if request.method == 'POST':
        todo_id = request.POST.get('id')
        new_todo_type = request.POST.get('todo_type')

        try:
            todo = Todo.objects.get(id=todo_id)
            todo.todo_type = new_todo_type
            todo.save()
            return JsonResponse({'status': 'success'})
        except Todo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Todo not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def update_todo_text(request):
    if request.method == 'POST':
        todo_id = request.POST.get('id')
        new_text = request.POST.get('text')

        try:
            todo = Todo.objects.get(id=todo_id)
            todo.text = new_text
            todo.save()
            return JsonResponse({'status': 'success'})
        except Todo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Todo not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


def delete_todo_task(request):
    if request.method == 'POST':
        todo_id = request.POST.get('id')

        try:
            todo = Todo.objects.get(id=todo_id)
            todo.delete()
            return JsonResponse({'status': 'success'})
        except Todo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Todo not found'}, status=404)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
