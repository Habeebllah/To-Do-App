from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
from django.http import HttpResponseRedirect



# Create your views here.
def home(request):
    todo_item = Todo.objects.all().order_by("-added_date_time")
    stuff_for_frontend = {'todo_item': todo_item}
    template_name = 'App/index.html'
    return render(request, template_name, stuff_for_frontend)


def add_todo(request):
    content = request.POST["content"]
    added_date = timezone.now()
    Todo.objects.create(text=content, added_date_time=added_date)
    template_name = 'App/index.html'
    stuff_for_frontend = {'content': content, }
    return HttpResponseRedirect("/")

def delete_item(request, pk):
    Todo.objects.get(id=pk).delete()
    return HttpResponseRedirect("/")




