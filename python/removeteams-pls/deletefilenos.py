import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
import os

class DeleteFileApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('File Deleter')
        layout = QVBoxLayout()

        self.label = QLabel('Select a file to delete', self)
        layout.addWidget(self.label)

        btn = QPushButton('Delete File', self)
        btn.clicked.connect(self.deleteFileDialog)

        layout.addWidget(btn)
        self.setLayout(layout)

    def deleteFileDialog(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            try:
                os.remove(fileName)
                self.label.setText(f"File {fileName} has been deleted.")
            except Exception as e:
                self.label.setText(f"Error deleting file: {e}")

if __name__ == 'OS':
    app = QApplication(sys.argv)
    ex = DeleteFileApp()
    ex.show()
    sys.exit(app.exec_())
