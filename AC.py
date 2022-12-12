import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI_AC import *

# 电源状况: 1 = 开 ,0 = 关
power = 0
mode = "cool"


class AC(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(AC, self).__init__(parent)
        self.setupUi(self)
        self._initUI()
        self.pushButton_4.mousePressEvent = self.tem_down
        self.pushButton_5.mousePressEvent = self.tem_up
        self.pushButton_2.mousePressEvent = self.mode_switch_to_cool
        self.pushButton_3.mousePressEvent = self.mode_switch_to_hot
        self.pushButton.mousePressEvent = self.power_switch
        self.pushButton_7.mousePressEvent = self.minesize

    def _initUI(self):
        _startPos = None
        _endPos = None
        _isTracking = False
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.show()

    def mouseMoveEvent(self, e: QMouseEvent):
        try:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)
        except:
            pass

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def tem_up(self, event):
        tem = int(self.label_shuzi.text())
        if power == 1 and 17 <= tem < 30:

            new_tem = str(tem + 1)
            self.label_shuzi.setText(new_tem)
        else:
            pass

    def tem_down(self, event):
        tem = int(self.label_shuzi.text())
        if power == 1 and 17 < tem <= 30:

            new_tem = str(tem - 1)
            self.label_shuzi.setText(new_tem)
        else:
            pass

    def power_switch(self, event):
        global power
        if power == 1:
            self.label_shuzi.setText("00")
            self.label_shuzi.setStyleSheet(
                "border-radius: 0px;  border: 0px groove black ;color: white"
            )
            self.frame_4.setStyleSheet("border-radius: 5px; border: 2px groove black")
            self.frame_3.setStyleSheet("border-radius: 5px; border: 2px groove black")

            power = 0
        elif power == 0:
            self.label_shuzi.setText("26")
            self.label_shuzi.setStyleSheet(
                "border-radius: 0px;  border: 0px groove black ;color: black"
            )
            self.frame_4.setStyleSheet(
                "border-radius: 5px;  background:blue;border: 0px groove black"
            )
            self.frame_3.setStyleSheet(
                "border-radius: 5px;  background:black;border: 0px groove black"
            )

            power = 1

    def mode_switch_to_hot(self, event):
        global power
        if power == 1:
            self.frame_4.setStyleSheet(
                "border-radius: 5px;  background:red ; border: 0px groove black"
            )
            self.label_shuzi.setText("26")
        else:
            pass

    def mode_switch_to_cool(self, event):
        global power
        if power == 1:
            self.frame_4.setStyleSheet(
                "border-radius: 5px;  background:blue ; border: 0px groove black"
            )
            self.label_shuzi.setText("20")
        else:
            pass

    def minesize(self, event):
        self.showMinimized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = AC()
    sys.exit(app.exec_())
