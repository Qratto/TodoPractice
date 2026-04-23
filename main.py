def indentation_symbol(func):
    def wrapper(task_id, task_value):
        print("======== \n" + func(task_id, task_value)  + "\n" + "======== \n")
        return None
    return wrapper

@indentation_symbol
def update_task(task_id, task_value):
    global tasks
    if not tasks:
        return "Задач нет"
    if not task_id in list(tasks.keys()):
        return "Такой задачи нет"
    tasks[task_id] = task_value
    return "Задача обновлена"

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
        pass
    elif action == 2:
        pass
    elif action == 3:
        print("Введите номер задачи: ", end="")
        task_id = int(input())
        print("Введите Еновую задачу: ", end="")
        task_value = input()
        update_task(task_id, task_value)
    elif action == 4:
        pass
    elif action == 5:
        break
    else:
        print("Неправильный ввод")
