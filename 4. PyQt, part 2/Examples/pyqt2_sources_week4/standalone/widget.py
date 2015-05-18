from PySide.QtCore import *
from PySide.QtGui import *
import sys, os
from ctypes import *

def getRootDir(*args):
    if getattr(sys, 'frozen', False):
        application_path = toLongName(os.path.abspath(os.path.dirname(sys.executable)))
    else:
        application_path = os.path.dirname(__file__)
    if args:
        application_path = os.path.join(application_path, os.path.join(*args))
    application_path = application_path.replace('\\','/')
    return application_path

def toLongName(path):
    '''
    from dos 8.3 format
    '''
    buf = create_unicode_buffer(500)
    windll.kernel32.GetLongPathNameW(unicode(path), buf, 500)
    return buf.value

class widgetClass(QWidget):
    def __init__(self):
        super(widgetClass, self).__init__()
        self.ly = QVBoxLayout(self)
        self.i = 0
        self.btn = QPushButton('Click')
        self.ly.addWidget(self.btn)
        self.btn.clicked.connect(self.hello)

    def hello(self):
        path = getRootDir()
        img = QFileDialog.getOpenFileName(self, 'Open file', path)
        if img[0]:
            i = QPixmap(img[0]).scaled(500,500)
            out = os.path.join(path, 'scaled.jpg')
            i.save(out, 'JPG')

if __name__ == '__main__':
    app = QApplication([])
    if getattr(sys, 'frozen', False):
        QApplication.addLibraryPath(sys._MEIPASS)
    w = widgetClass()
    w.show()
    app.exec_()