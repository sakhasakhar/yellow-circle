import sys
from PyQt5 import uic
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Жолтые окружности....`')
        self.do_paint = False
        self.drawBtn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        qp.setPen(QColor(255, 255, 0))
        r = randrange(20, 250)
        qp.drawEllipse(250 - r, 250 - r, r * 2, r * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
