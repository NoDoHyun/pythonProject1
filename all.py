import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtWidgets
import urllib.request
from jangduk import FirstClass
from test import testClass
import webbrowser
import csv
import random
form_class = uic.loadUiType("title.ui")[0]
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.widget.pushButton_4.clicked.connect(self.next)
    def next(self):
        print("!!!!!!!!!!")
        widget.setCurrentIndex(2)
if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    my = WindowClass
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    #WindowClass의 인스턴스 생성
    firstpage = FirstClass()
    testlogin = testClass()

    #프로그램 화면을 보여주는 코드

    widget.addWidget(firstpage)
    widget.addWidget(testlogin)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()