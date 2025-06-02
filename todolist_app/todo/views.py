# todo/views.py
from django.shortcuts import render, redirect
from .models import ToDoItem

# ToDoアイテムのリストを取得
def todo_list(request):
    todos = ToDoItem.objects.all() # todosという変数にToDoItem.objects.all()を格納している
    ###########################################################################################
    """ todo_item = ToDoItem.objects.get(id=65)
    print(todo_item.title)
    print(todo_item.description) """
    ###########################################################################################
    # print(todos.last().title)
    # print(todos.last().description)
    # valueのリストを作成
    response = []
    for todo in todos.values():
        # print("説明", todo) 
        response.append(todo)
    # return render(request, 'todo/todo_list.html', {'todos': [{"title": ToDoItem.objects.all(), "description": ToDoItem.objects.all () }]})
    return render(request, 'todo/todo_list.html', {'todos': response})

#リストの追加
def add_todo(request):
    # print(request.method)
    if request.method == 'POST':
        # print('post')
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title and description:
            # print('ok')
            todo_item = ToDoItem(title=title, description=description)
            todo_item.save()
            # print(ToDoItem.objects.last().description)
        return render(request, 'todo/add_todo.html')
        
    # print('not')
    return render(request, 'todo/add_todo.html')

#リストの編集
def edit_todo(request,):
    todo_item = ToDoItem.objects.get(id='62')
    ###########################################################################################
    """ print(todo_item.title)
    print(todo_item.description)
    print(todo_item.id) """
    ##########################################################################################
    if request.method == "GET":
        print('get')
        return render(request, 'todo/edit_todo.html', {'todo_item': todo_item}) #edit_todo.htmlにtodo_itemの変数を渡す。これによってtodo_itemの情報を表示できるようになる。
    ###########################################################################################
    if request.method == "POST":
        print('post')
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            todo_item.title = request.POST.get('title')
            todo_item.description = request.POST.get('description')
            print(todo_item.title)
            todo_item.save()
        return redirect('todo:edit_todo')
    return render(request, 'todo/edit_todo.html')


#リストの削除
def delete_todo(request, todo_id):
    return render(request, 'todo/delete_todo.html')

#リストの表示
def index(request):
    # print(ToDoItem.objects.all())
    return render(request, 'todo/index.html')
