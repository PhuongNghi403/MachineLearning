from PyQt6.QtWidgets import QApplication
from dataprocessing.MainWindowEx import MainWindowEx

app = QApplication([])
myWindow = MainWindowEx()
myWindow.show()
app.exec()
