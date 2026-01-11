from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLabel, QLineEdit, QPushButton, QListWidget
)
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My To-Do App")

layout = QVBoxLayout()

label = QLabel("Type in to-do")
entry = QLineEdit()
button = QPushButton("Add")
listbox = QListWidget()

def add_todo():
    text = entry.text()
    if text:
        listbox.addItem(text)
        entry.clear()

button.clicked.connect(add_todo)

layout.addWidget(label)
layout.addWidget(entry)
layout.addWidget(button)
layout.addWidget(listbox)

window.setLayout(layout)
window.show()

sys.exit(app.exec())
