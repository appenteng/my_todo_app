import customtkinter as ctk

def add_todo():
    todo = entry.get()
    if todo:
        listbox.insert("end", todo)
        entry.delete(0, "end")

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("My To-Do App")

ctk.CTkLabel(root, text="Type in to-do").pack(pady=5)

entry = ctk.CTkEntry(root)
entry.pack(pady=5)

ctk.CTkButton(root, text="Add", command=add_todo).pack(pady=5)

listbox = ctk.CTkTextbox(root, width=300, height=200)
listbox.pack()

root.mainloop()
