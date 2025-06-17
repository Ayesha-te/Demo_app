from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import ToDo, Task, Grade

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

@login_required
def dashboard_view(request):
    todos = ToDo.objects.filter(user=request.user)
    tasks = Task.objects.filter(user=request.user)
    grades = Grade.objects.filter(user=request.user)

    return render(request, 'dashboard.html', {
        'todos': todos,
        'tasks': tasks,
        'grades': grades
    })

@login_required
def add_todo(request):
    if request.method == 'POST':
        ToDo.objects.create(user=request.user, text=request.POST['todo'])
    return redirect('dashboard')

@login_required
def add_task(request):
    if request.method == 'POST':
        Task.objects.create(user=request.user, text=request.POST['task'])
    return redirect('dashboard')

@login_required
def add_grade(request):
    if request.method == 'POST':
        Grade.objects.create(
            user=request.user,
            subject=request.POST['subject'],
            grade=request.POST['grade']
        )
    return redirect('dashboard')

def logout_view(request):
    logout(request)
    return redirect('login')
from django.shortcuts import render

def frontend_page(request):
    return render(request, "frontend.html")
