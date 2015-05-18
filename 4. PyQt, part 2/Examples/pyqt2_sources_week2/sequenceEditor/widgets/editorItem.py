from PySide.QtCore import *
from PySide.QtGui import *


class editorItemClass(QGraphicsItem):
    def __init__(self, height, num):
        super(editorItemClass, self).__init__()
        self.x = 0
        self.y = 0
        self.w = 150
        self.h = height
        self.num = num
        self.hover = None
        self.setAcceptHoverEvents(True)
        self.resizePadding = 10
        self.resizeL = False
        self.resizeR = False
        self.startPos = None
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

    def boundingRect(self):
        return QRect(self.x, self.y, self.w, self.h)

    def paint(self, painter, opt, w):
        rec = self.boundingRect()
        if False:
            painter = QPainter()
        painter.fillRect(rec, Qt.black)
        painter.fillRect(rec.adjusted(1,1,-1,-1), Qt.white)
        if not self.hover:
            color = Qt.darkGray
        else:
            color = Qt.gray
        if self.isSelected():
            color = Qt.yellow
        painter.fillRect(rec.adjusted(3,3,-3,-3), color)

        painter.setFont(QFont('Arial', 10))
        painter.setPen(QPen(Qt.black))
        painter.drawText(rec, Qt.AlignCenter, 'Node %s' % self.num)

        painter.setPen(Qt.NoPen)

        painter.fillRect(QRect(self.x+4,4,self.resizePadding, self.h-8), Qt.red)
        painter.fillRect(QRect(self.x+self.w-4-self.resizePadding,4,self.resizePadding, self.h-8), Qt.red)


    def adjustpos(self):
        y = self.pos().y()
        delta = y % self.h
        if delta > self.h / 2:
            delta = self.h-delta
            self.setPos(self.pos()+QPoint(0, delta))
        else:
            self.setPos(self.pos()-QPoint(0, delta))

    def checkCollision(self):
        coll =self.scene().collidingItems(self)
        if coll:
            self.setPos(self.pos()-QPoint(0, self.h))
            self.checkCollision()

    def hoverMoveEvent(self, event):
        p = event.pos().x()
        if self.x < p < self.x+self.resizePadding:
            self.setCursor(Qt.SizeHorCursor)
            self.resizeL = True
        elif self.x+self.w - self.resizePadding < p < self.w+self.x:
            self.setCursor(Qt.SizeHorCursor)
            self.resizeR = True
        else:
            self.setCursor(Qt.SizeAllCursor)
            self.resizeR = self.resizeL = False
        super(editorItemClass, self).hoverMoveEvent(event)

    def hoverEnterEvent(self, event):
        self.hover = True
        super(editorItemClass, self).hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.hover = False
        super(editorItemClass, self).hoverLeaveEvent(event)

    def mousePressEvent(self, event):
        self.startPos = event.pos()
        super(editorItemClass, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.resizeL or self.resizeR:
            delta = (self.startPos - event.pos()).x()
            self.startPos = event.pos()
            if self.resizeL:
                tmp1 = self.x
                tmp2 = self.w
                self.x = self.x - delta
                self.w = self.w + delta
                if self.scene().collidingItems(self):
                    self.x = tmp1
                    self.w = tmp2
            else:
                tmp = self.w
                self.w -= delta
                if self.scene().collidingItems(self):
                    self.w = tmp
            self.scene().update()
        else:
            super(editorItemClass, self).mouseMoveEvent(event)