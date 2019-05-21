import sys

from PyQt5 import QtWidgets
from ui import Ui_MainWindow


class Main(QtWidgets.QMainWindow):
    algorithms = ['', 'Algorithm 1', 'Algorithm 2']

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButtonSelectFile.pressed.connect(self.select_file)
        self.ui.comboBoxSelectAlgorithm.addItems(self.algorithms)
        self.ui.pushButtonResult.pressed.connect(self.show_result)

    def select_file(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, 'QFileDialog.getOpenFileName()', './samples',
            'All Files (*);;', options=options
        )

    def show_result(self):
        self.ui.labelForResult.setText('RESULT')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Main()
    MainWindow.show()
    sys.exit(app.exec_())
