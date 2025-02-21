from django.forms import ModelForm
from .models import ToDoItem

class ToDoForm(ModelForm):
    class mata:
        model = ToDoItem
        fields = ['title', 'description']