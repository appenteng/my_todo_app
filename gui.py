from numpy.lib.function_base import blackman

import functions
import PySimpleGUI as sg
import time

sg.theme('black')
clock = sg.Text('',key='clock')
label = sg.Text("Type in to-do")
input_box = sg.Input(tooltip="Enter todo here", key='todo')
button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos',
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My To-Do App",
                   layout=[[clock],
                            [label, input_box, button],
                   [list_box, edit_button,complete_button],
                    [exit_button]],
                     font=('Helvetica', 12))
while True:
    event, values =window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case "Add":
            try:
                todos = functions.get_todos()
                new_todo = values['todo'] + "\n"
                todos.append(new_todo)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
                if new_todo.strip() == "":
                    raise ValueError("Empty to-do item")
            except ValueError as ve:
                sg.popup(f"Error: {ve}", font=('Helvetica', 20))
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo= values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item to edit.", font=('Helvetica', 20))
        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item to complete.", font=('Helvetica', 20))
        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()