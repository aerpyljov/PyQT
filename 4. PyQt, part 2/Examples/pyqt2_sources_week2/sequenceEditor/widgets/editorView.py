from PySide.QtCore import *
from PySide.QtGui import *
import editorScene


class editorViewClass(QGraphicsView):
    def __init__(self):
        super(editorViewClass, self).__init__()
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.s = editorScene.editorSceneClass()
        self.setScene(self.s)

        self.pan = False
        self.lastX = 0
        self.lasty = 0

    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.pan = True
            self.lastX = event.x()
            self.lastY = event.y()
        else:
            super(editorViewClass, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.pan:
            self.setInteractive(False)
            valX = self.horizontalScrollBar().value() - (event.x() - self.lastX)
            self.horizontalScrollBar().setValue(valX)
            self.lastX = event.x()

            valY = self.verticalScrollBar().value() - (event.y() - self.lastY)
            self.verticalScrollBar().setValue(valY)
            self.lastY = event.y()
            self.setInteractive(True)
        else:
            super(editorViewClass, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self,event):
        super(editorViewClass, self).mouseReleaseEvent(event)
        self.pan = False