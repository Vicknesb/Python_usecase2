from django.contrib import admin
from .models import Register, TodoList, TodoItem

# Register your models here.
# class Registeradmin(admin.ModelAdmin):
#  list_display = ("Username");

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("title", "description");

admin.site.register(Register)
admin.site.register(TodoList)
admin.site.register(TodoItem, TodoItemAdmin)