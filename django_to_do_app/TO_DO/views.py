from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from datetime import date, time, datetime
from .models import TodoList
from django.shortcuts import get_object_or_404


def AddToDo(request):
    if request.method == "POST":
        if request.POST.get('todo_name'):
            SaveRecord = TodoList()
            todo_name = request.POST.get('todo_name')
            formated_name = todo_name.title()
            SaveRecord.todo_name = formated_name
            SaveRecord.timestamps = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
            SaveRecord.is_completed = "No"
            he = request.POST.get('todo_status')
            print("---------------------", he)
            SaveRecord.save()
            messages.success(request, "New Todo Has Been Added !")

    todos = TodoList.objects.filter(is_completed="No").order_by('id')

    return render(request, 'pages/todo.html', {'todos': todos})


def ViewTodo(request):
    todos = TodoList.objects.filter(is_completed="No").order_by('id')
    print(todos)

    return render(request, 'pages/todo.html', {'todos': todos})


def EditTodo(request, todo_id):
    edited_todo = request.POST.get('edited_todo')
    todo = get_object_or_404(TodoList, id=todo_id)
    todo.todo_name = edited_todo
    todo.save()
    messages.success(request, "Todo Edited ")
    todos = TodoList.objects.filter(is_completed="No").order_by('id')

    return render(request, 'pages/todo.html', {'todos': todos})


def CompleteTodo(request, todo_id):
    todo = get_object_or_404(TodoList, id=todo_id)
    todo.is_completed = "Yes"
    todo.save()
    messages.success(request, "Congratulations, You are ahead one step !!")
    todos = TodoList.objects.filter(is_completed="No").order_by('id')

    return render(request, 'pages/todo.html', {'todos': todos})


# def SearchTodo(request):
#     print(".......... Before checking POST method")
#     if request.method == "POST":
#         print(".......... After checking POST method")
#         if request.POST.get('todo_status'):
#             todo_status = request.POST.get('todo_status_name')
#             print(">>>>>>>>>>>", todo_status)
#
#  return render(request, 'pages/todo.html')

def SearchTodo(request):
    print(">>>>>>>>>>>Before")
    h = TodoList.objects.none()
    if request.method == "POST":
        todo_status = request.POST.get('todo_status')
        if todo_status == 'Completed':
            h = TodoList.objects.filter(is_completed="Yes").order_by('-id')
        elif todo_status == 'Pending':
            h = TodoList.objects.filter(is_completed="No").order_by('-id')
        else:
            h = TodoList.objects.all().order_by('-id')
    todos = h
    print(">>>>>>>>>>>----", todos)
    return render(request, 'pages/search_todo.html', {'todos': todos})


def Demo(request):
    print(">>>>>>>>>>>Before")
    h = TodoList.objects.none()
    if request.method == "POST":
        todo_status = request.POST.get('todo_status')
        if todo_status == 'Completed':
            h = TodoList.objects.filter(is_completed="Yes").order_by('-id')
        elif todo_status == 'Pending':
            h = TodoList.objects.filter(is_completed="No").order_by('-id')
        else:
            h = TodoList.objects.all().order_by('-id')
    todos = h
    print(">>>>>>>>>>>----", todos)
    return render(request, 'pages/demo.html', {'todos': todos})
