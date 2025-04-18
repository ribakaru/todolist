# todo/views.py
from django.shortcuts import render, redirect
from .models import ToDoItem

# ToDoアイテムのリストを取得
def todo_list(request):
    todos = ToDoItem.objects.all()
    print(todos.last().title)
    print(todos.last().description)
    return render(request, 'todo/todo_list.html', {'todos': [{"title": "", "description": ""}]})

#リストの追加
def add_todo(request):
    print(request.method)
    if request.method == 'POST':
        print('post')
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            print('ok')
            todo_item = ToDoItem(title=title, description=description)
            todo_item.save()
        return render(request, 'todo/add_todo.html')
        
    print('not')
    return render(request, 'todo/add_todo.html')

#リストの編集
def edit_todo(request, todo_id):
    response = "You're edting the todo item %s."
    return render(request, 'todo/edit_todo.html', {'todo_item'}) 

#リストの削除
def delete_todo(request, todo_id):
    todo_item = ToDoItem.objects.get(id=todo_id) #idを取得
    todo_item.delete() #削除
    return redirect('todo_list') #リストを削除

#リストの表示
def index(request):
    print(ToDoItem.objects.all())
    return render(request, 'todo/index.html')
