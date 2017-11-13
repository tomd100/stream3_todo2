from django import forms
from .models import TodoItem, LoginItem

class TodoItemForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ('name', 'priority', 'done')
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = LoginItem
        fields = ('name', 'password')