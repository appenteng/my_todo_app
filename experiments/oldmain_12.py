from functions import get_todos, write_todos

while True:
    user_action = input("type add, show, edit, remove or exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        todos= get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_action.startswith("show"):

        todos=get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[4:])
            print(number)

            number = number - 1

            todos=get_todos()

            new_todo = input("enter new todo: ") + "\n"
            todos[number] = new_todo

            write_todos(todos)

            print(new_todo.strip())
        except ValueError:
            print('You entered wrong command')
            continue

    elif user_action.startswith('delete' or 'remove'):
        try:
            number_str = user_action[7:].strip()

            todos=get_todos()

            number = int(number_str)
            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f'todo {todos_to_remove} was removed from the list.'
        except IndexError:
            print('there is no item with that number')
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('command is invalid')

print("bye bye")
