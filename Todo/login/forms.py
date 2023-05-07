from django import forms
from .models import Login, Register, TodoList, TodoItem

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__'

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = '__all__'