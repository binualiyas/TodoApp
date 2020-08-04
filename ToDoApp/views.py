from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm


# Create your views here.
def index(request):
    return render(request,'ToDoApp/index.html')

@login_required(login_url='/')  
def home(request):
    todo_list=Todo.objects.order_by('id')
    form= TodoForm()
    context={'todo_list':todo_list,'form':form}
    return render(request,'ToDoApp/home.html', context)


@require_POST
def addTodo(request):
    form =TodoForm(request.POST)
    if form.is_valid():
        new_todo=Todo(text=request.POST['text'])
        new_todo.save() 
    #print(request.POST['text'])
    return redirect('home')

def completeTodo(request, todo_id):
    #todo_id=int(todo_id)
    todo=Todo.objects.get(pk=todo_id)
    todo.complete=True
    
    todo.save()
    return redirect('home')

def deleteComplete(request):
    #todo=Todo.objects.filter(complete=True).delete() 
    Todo.objects.filter(complete=True).delete() 
    return redirect('home')

def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('home')

def registerView(request):
    if request.method == "POST":
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form= UserCreationForm()
    return render(request,'ToDoApp/register.html',{'form':form})


def dashboardView(request):
    return render(request,'ToDoApp/dashboard.html')