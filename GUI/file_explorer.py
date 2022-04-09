from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QWidget


class FileExplorer(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'File Explorer'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, 400, 300)

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "File Explorer", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        return fileName