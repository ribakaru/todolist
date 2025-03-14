# todo/views.py
from django.shortcuts import render, redirect
from .models import ToDoItem

# ToDoアイテムのリストを取得
def todo_list(request):
    todos = ToDoItem.objects.all()
    print(todos.last().title)
    print(todos.last().description)
    return render(request, 'todo/todo_list.html', {'todos': [{"title": "タイトル", "description": "説明"}]})

#リストの追加
def add_todo(request):
    print(request.method)
    if request.method == 'POST': #POSTメソッドであるかどうかを判断
        print("POSTメソッドです")
        title = request.POST.get('title') #titleを取得
        print(title)
        description = request.POST.get('description') #descriptionを取得
        print(description)
        todo_item = ToDoItem(title="テストタイトル", description="テスト説明") #ToDoItemを作成
        title == 'POST' #POSTメソッドであるかどうかを判断
        todo_item.save() #保存
        return redirect('/') #リストを追加

    print("GETメソッドです")
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
