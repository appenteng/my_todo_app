todos=[]

while True:
    user_action = input("type add, show, edit, remove or exit: ")
    user_action = user_action.strip().lower()
    match user_action:
        case "add":
            todo = input("enter a todo: ") + "\n"
            todos.append(todo)
            file=open("todos.txt","w+")
            file.writelines(todos)


        case "show" | "display":
            for index ,item in enumerate(todos, start=1):
              row=f"{index}.{item}"
              print(row)
        case "edit":
            number=int(input("enter a number of the todo: "))
            number=number -1
            new_todo =input("enter new todo: ")
            todos[number]=new_todo
            print(new_todo)

        case "exit":
            todos.clear()
            break
        case 'remove' | 'complete' | 'delete':
            number = int(input("enter a number of the todo: "))
            todos.pop(number -1)
            print(todos)


        case whatever:
            print("hey, you typed the wrong input")
print ("bye bye")
