from PySide.QtCore import *
from PySide.QtGui import *


class simpleWidget(QWidget):
    def __init__(self):
        super(simpleWidget, self).__init__()
        ly = QVBoxLayout(self)
        self.label = QLabel('OUT')
        ly.addWidget(self.label)
        self.installEventFilter(self)
        self.removeEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Enter:
            self.label.setText('IN')
            return True
        elif event.type() == QEvent.Leave:
            self.label.setText('OUT')
            return True
        return False

if __name__ == '__main__':
    app = QApplication([])
    w = simpleWidget()
    w.show()
    app.exec_()