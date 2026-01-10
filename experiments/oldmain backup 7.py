while True:
    user_action = input("type add, show, edit, remove or exit: ")
    user_action = user_action.strip().lower()

    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

        case "show" | "display":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()


            for index, item in enumerate(todos, start=1):
               row = f"{index}. {item.strip()}"
               print(row)

        case "edit":
            number = int(input("enter a number of the todo: "))
            number = number - 1
            new_todo = input("enter new todo: ") + "\n"
            todos[number] = new_todo

            print(new_todo.strip())

        case 'remove' | 'complete' | 'delete':
            number = int(input("enter a number of the todo: "))
            todos.pop(number - 1)
            print("Todo removed")

        case "exit":
            todos.clear()
            break

        case _:
            print("hey, you typed the wrong input")

print("bye bye")
