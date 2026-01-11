import tkinter as tk

def add_todo():
    todo = entry.get()
    if todo:
        listbox.insert(tk.END, todo)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("My To-Do App")

tk.Label(root, text="Type in to-do").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Add", command=add_todo).pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack()

root.mainloop()
