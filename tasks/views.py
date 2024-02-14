from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import auth, User
from django.contrib import messages


@login_required(login_url='login')
def index(request):
    tasks = Tasks.objects.all()

    form = TasksForm()

    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {"tasks": tasks, "form": form}
    return render(request, 'tasks/list_todo.html', context)


@login_required(login_url='login')
def update_task(request, pk):

    task = Tasks.objects.get(id=pk)
    form = TasksForm(instance=task)

    if request.method == 'POST':
        form = TasksForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        "form": form
    }

    return render(request, 'tasks/update_task.html', context)


@login_required(login_url='login')
def delete_task(request, pk):
    item = Tasks.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}

    return render(request, 'tasks/delete.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('list')
        else:
            messages.info(request, 'Credentials Invalid')
            redirect('list')

    return render(request, 'tasks/login.html')


def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                return redirect('/')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')

    return render(request, 'tasks/signup.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('logout')



