from PySide6.QtWidgets import QApplication, QLabel
import sys

app = QApplication(sys.argv)
label = QLabel("PySide6 works!")
label.show()
sys.exit(app.exec())
