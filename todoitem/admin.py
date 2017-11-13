from django.contrib import admin
from .models import TodoItem     # . means it is in this app

# Register your models here.
admin.site.register(TodoItem);


