# todo/views.py
from django.shortcuts import render, redirect
from .models import ToDoItem

# ToDoアイテムのリストを取得
def todo_list(request):
    todos = ToDoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

#リストの追加
def add_todo(request):
    if request.method == 'POST': #POSTメソッドであるかどうかを判断
        title = request.POST.get('title') #titleを取得
        description = request.POST.get('description') #descriptionを取得
        todo_item = ToDoItem(title=title, description=description) #ToDoItemを作成
        title == 'POST' #POSTメソッドであるかどうかを判断
        todo_item.save() #保存
        return redirect('todo_list') #リストを追加
    return render(request, 'todo/add_todo.html')

#リストの編集
def edit_todo(request, todo_id):
    todo_item = ToDoItem.objects.get(id=todo_id) #idを取得
    return render(request, 'todo/edit_todo.html', {'todo_item': todo_item}) #リストを編集する

#リストの削除
def delete_todo(request, todo_id):
    todo_item = ToDoItem.objects.get(id=todo_id) #idを取得
    todo_item.delete() #削除
    return redirect('todo_list') #リストを削除

#リストの表示
def index(request):
    return render(request, 'todo/index.html')
