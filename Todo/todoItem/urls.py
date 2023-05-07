from django.urls import path
from . import views

urlpatterns =[
    path("", views.createtodo),
    path("todoitem", views.create_item),
    path("tododetails", views.get_itemId),
    path("/<id>", views.get_todo_list),
    path("todoitems/<id>", views.get_todo_item),
    path("todolistdelete/<id>", views.tododelete, name="listdelete"),
    path("todoitemdelete/<id>", views.todoitem_delete, name="itemdelete")
]