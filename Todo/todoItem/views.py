from django.shortcuts import render
from login.forms import TodoListForm, TodoItemForm
from login.models import TodoItem, TodoList
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

def createtodo(request):
    if (request.method == "POST"):
        form = TodoListForm(request.POST)

        if form.is_valid():
          todolist = TodoList(title = form.cleaned_data['title'], description =form.cleaned_data['description'])
          todolist.save()
          return HttpResponseRedirect('/tododetails') 
    else:
         todoform = TodoListForm()
         return render(request, 'todo_grid.html',{
            "todo_data": todoform,
         })

def create_item(request):
    if (request.method == "POST"):
         formtodo = TodoItemForm(request.POST)
         if formtodo.is_valid():
          todoItem = TodoItem(title = formtodo.cleaned_data['title'], 
                              description = formtodo.cleaned_data['description'],
                              duedate = formtodo.cleaned_data['duedate'],
                              is_complete = formtodo.cleaned_data['is_complete'],
                              todolist = formtodo.cleaned_data['todolist'])
          todoItem.save()
          return HttpResponseRedirect('/tododetails') 
    else:
         todoitemform = TodoItemForm()
         return render(request, 'todo_item.html',{
            "item_data": todoitemform
        })
    
def get_itemId(request):
    tododetails = TodoList.objects.all().order_by('-id')
    todoitemdetails = TodoItem.objects.all().order_by('-id')
    return render(request, "todo_item_details.html",{
        "forms": tododetails,
        "item_data": todoitemdetails
    })

def get_todo_list(request, id):
    try:
        if (request.method == "POST"):
            form = TodoListForm(request.POST)

            if form.is_valid():
                tododetails = TodoList.objects.get(id=id)
                tododetails.title = form.cleaned_data['title']
                tododetails.description = form.cleaned_data['description']
                tododetails.save()
                return HttpResponseRedirect('/tododetails') 
        else:
            tododetails = TodoList.objects.get(id=id)
            form = TodoListForm()
            form.initial['title'] = tododetails.title
            form.initial['description'] = tododetails.description
            return HttpResponseRedirect('/tododetails') 
    except:
        return HttpResponseNotFound("No records found")

def get_todo_item(request, id):
    if (request.method == "POST"):
        form = TodoItemForm(request.POST)

        if form.is_valid():
          tododetails = TodoItem.objects.get(id=id)
          tododetails.title = form.cleaned_data['title']
          tododetails.description = form.cleaned_data['description']
          tododetails.duedate = form.cleaned_data['duedate']
          tododetails.save()
          return HttpResponseRedirect('/tododetails') 
    else:
     tododetails = TodoItem.objects.get(id=id)
     form = TodoItemForm()
     form.initial['title'] = tododetails.title
     form.initial['description'] = tododetails.description
     form.initial['duedate'] = tododetails.duedate
     form.initial['is_complete'] = tododetails.is_complete
     form.initial['todolist'] = tododetails.todolist

    return render(request, "todo_item.html", {
        "item_data":form
    })

def tododelete(request, id):
    tododetails = TodoList.objects.get(id=id)
    tododetails.delete()
    return HttpResponseRedirect('/tododetails') 

def todoitem_delete(request, id):
    tododetails = TodoItem.objects.get(id=id)
    tododetails.delete()
    return HttpResponseRedirect('/tododetails') 
