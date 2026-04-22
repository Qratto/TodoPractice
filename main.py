def indentation_symbol(func):
    def wrapper():
        print("======== \n" + func() + "======== \n")
        return None
    return wrapper

def create_task(value):
    global tasks
    if not tasks:
        tasks[1] = value
        return "Задача создана"
    current_id = list(tasks.keys())[-1]
    tasks[f"{int(current_id)+1}"] = value
    return "Задача создана"

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
        print("Введите задача: ", end="")
        task = input()
        create_task(task)
    elif action == 3:
        pass
    elif action == 4:
        pass
    elif action == 5:
        break
    else:
        print("Неправильный ввод")
