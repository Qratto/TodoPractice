def indentation_symbol(func):
    def wrapper(task_id):
        print("======== \n" + func(task_id) + "\n" + "======== \n")
        return None
    return wrapper

@indentation_symbol
def delete_task(task_id):
    global tasks
    if not task_id in list(tasks.keys()):
        return "Такой задачи нет"
    tasks.pop(task_id)
    return "Задача удалена"
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
        pass
    elif action == 4:
        print("Введите номер задачи ", end="")
        task_id = int(input())
        delete_task(task_id)
    elif action == 5:
        break
    else:
        print("Неправильный ввод")
