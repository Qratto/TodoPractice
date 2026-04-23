def indentation_symbol_delete(func):
    def wrapper(task_id):
        print("======== \n" + func(task_id) + "\n" + "======== \n")
        return None
    return wrapper

@indentation_symbol_delete
def delete_task(task_id):
    global tasks
    if not task_id in list(tasks.keys()):
        return "Такой задачи нет"
    tasks.pop(task_id)
    return "Задача удалена"

def indentation_symbol_update(func):
    def wrapper(task_id, task_value):
        print("======== \n" + func(task_id, task_value)  + "\n" + "======== \n")
        return None
    return wrapper

@indentation_symbol_update
def update_task(task_id, task_value):
    global tasks
    if not tasks:
        return "Задач нет"
    if not task_id in list(tasks.keys()):
        return "Такой задачи нет"
    tasks[task_id] = task_value
    return "Задача обновлена"

def indentation_symbol_create(func):
    def wrapper(task):
        print("======== \n" + func(task) + "\n" + "======== \n")
        return None
    return wrapper
  
def indentation_symbol(func):
    def wrapper():
        print("======== \n" + func() + "======== \n")
        return None
    return wrapper

@indentation_symbol_create
def create_task(value):
    global tasks
    if not tasks:
        tasks[1] = value
        return "Задача создана"
    current_id = list(tasks.keys())[-1]
    tasks[f"{int(current_id)+1}"] = value
    return "Задача создана"

@indentation_symbol
def view_tasks():
    global tasks
    return_text = ""
    if not tasks:
        return "Задач нет \n"
    for i, j in tasks.items():
        return_text += f"id: {i}, задача: {j} \n"
    return return_text

print("Приложение: Todo List")

tasks = {}

while True:
    print("1 - Просмотр задач \n"
          "2 - Создание задачи  \n"
          "3 - Изменение задачи \n"
          "4 - Удаление задачи \n"
          "5 - Выход из приложения \n"
          "Выберите действие ", end="")

    action = int(input())

    if action == 1:
        view_tasks()
    elif action == 2:
        print("Введите задача: ", end="")
        task = input()
        create_task(task)
    elif action == 3:
        print("Введите номер задачи: ", end="")
        task_id = int(input())
        print("Введите Еновую задачу: ", end="")
        task_value = input()
        update_task(task_id, task_value)
    elif action == 4:
        print("Введите номер задачи ", end="")
        task_id = int(input())
        delete_task(task_id)
    elif action == 5:
        break
    else:
        print("Неправильный ввод")
