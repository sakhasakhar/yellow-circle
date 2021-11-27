import sys
from PyQt5 import QtCore, QtWidgets
from random import randrange
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        Form.setStyleSheet("background-color: rgb(43, 85, 149)")
        self.drawBtn = QtWidgets.QPushButton(Form)
        self.drawBtn.setGeometry(QtCore.QRect(190, 440, 131, 31))
        self.drawBtn.setObjectName("drawBtn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.drawBtn.setText(_translate("Form", "Нарисовать"))


class Example(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        qp.setPen(QColor(randrange(255), randrange(255), randrange(255)))
        r = randrange(20, 250)
        qp.drawEllipse(250 - r, 250 - r, r * 2, r * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
