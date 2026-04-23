def indentation_symbol(func):
    def wrapper():
        print("======== \n" + func() + "======== \n")
        return None
    return wrapper

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
        pass
    elif action == 3:
        pass
    elif action == 4:
        pass
    elif action == 5:
        break
    else:
        print("Неправильный ввод")
