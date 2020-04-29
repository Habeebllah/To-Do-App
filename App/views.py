from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from django.http import HttpResponseRedirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    todo_item = Todo.objects.all().order_by("-created_at")
    context = {'todo_item': todo_item}
    template_name = 'App/index.html'
    return render(request, template_name, context)

@login_required(login_url='login')
def add_todo(request):
    template_name = 'App/index.html'
    form = TodoForm(request.POST or None)
    context = {'form': form, }
    if request.method == 'POST':
        form.is_valid()
        form.save()
        return redirect('home')
    return render(request, template_name, context)


'''
def add_item(request, pk):
    content = request.GET["content"]
    added_date = timezone.now()
    Todo.objects.filter(pk=pk).update(text=content, added_date_time=added_date)
    template_name = 'App/index.html'
    stuff_for_frontend = {'content': content, }
    return HttpResponseRedirect("/")
'''

@login_required(login_url='login')
def edit_item(request, pk):
    todo_item = Todo.objects.all().order_by("-created_at")
    item = get_object_or_404(Todo, pk=pk)
    form = TodoForm(request.POST or None, instance=item)
    template_name = 'App/update.html'
    context = {'todo_item': todo_item, 'form': form,}
    if request.method == 'POST':
        form.is_valid()
        form.save()
        return redirect('/')
    return render(request, template_name, context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + ' user account was created successfully')
            return redirect('login')

    context = {'form': form}
    template_name = 'App/register.html'
    return render(request, template_name, context)


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, ' username or password incorrect')

    template_name = 'App/login.html'
    return render(request, template_name)

@login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def delete_item(request, pk):
    Todo.objects.get(id=pk).delete()
    return HttpResponseRedirect("/")
