# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'title.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import urllib.request
from PyQt5 import uic
import webbrowser
import csv
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from login import WindowClass
form_class = uic.loadUiType("title.ui")[0]

class FirstClass(QMainWindow, form_class):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.img()
        self.txt()
        self.rebooks=[]
        self.pushButton_3.clicked.connect(self.back)
        self.pushButton_4.clicked.connect(self.login)
        self.pushButton_5.clicked.connect(self.page2)
        self.pushButton_6.clicked.connect(self.page3)
        self.pushButton_7.clicked.connect(self.page1)
        self.pushButton_10.clicked.connect(lambda: webbrowser.open('https://lib.gwangsan.go.kr/CD/scheduleMonth'))
        self.pushButton_8.clicked.connect(self.back)
        self.pushButton_9.clicked.connect(self.back)
        self.pushButton_11.clicked.connect(lambda: webbrowser.open('https://lib.gwangsan.go.kr/CD/board/3/1/read/3364?query='))
        self.pushButton_12.clicked.connect(lambda: webbrowser.open('https://lib.gwangsan.go.kr/CD/board/3/1/read/3350?query='))
        self.pushButton_13.clicked.connect(lambda: webbrowser.open('https://lib.gwangsan.go.kr/CD/board/3/1/read/3332?query='))
        self.pushButton_14.clicked.connect(lambda: webbrowser.open('https://lib.gwangsan.go.kr/CD/board/3/1/read/3330?query='))
        self.pushButton_15.clicked.connect(lambda: webbrowser.open('https://lib.gwangsan.go.kr/CD/board/3/1/read/3303?query='))
        self.pushButton_16.clicked.connect(lambda: webbrowser.open('https://lib.gwangsan.go.kr/CD/board/3/1/read/3259?query='))
        self.pushButton_17.clicked.connect(lambda: webbrowser.open('https://lib.gwangsan.go.kr/CD/board/3/1/read/3257?query='))
        self.stackedWidget.setCurrentIndex(0)
        self.reset.clicked.connect(self.resetb)
    def back(self):
        self.stackedWidget.setCurrentIndex(0)
    def page1(self):
        self.stackedWidget.setCurrentIndex(1)
    def page2(self):
        self.stackedWidget.setCurrentIndex(2)
    def page3(self):
        self.stackedWidget.setCurrentIndex(3)
    def img(self):
        # self.label_pic = QLabel(self)
        urlString = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAzMDRfMzQg%2FMDAxNjQ2Mzc5OTQ3MjU1.YfxpXyTx5SAgN8Er8NPKcY-lTPJbS3A9KGeSlniwIlsg.8aqlFU5woRzFwAQNwP2u1m2IwB8l_A_IzV_IV4ZIGbEg.JPEG.mkrs170812%2FKakaoTalk_20220304_164302211_01.jpg&type=sc960_832'
        urlString2= 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAzMzFfMTIg%2FMDAxNjE3MTM5NzU4ODk0.b_OAZ-pewoXj-F2l3xDstwyGlWjjc8rSfWjxIYEAyBYg.DbjxW2gRKCv8YcaFiiKAzk9hDMCKaofN4J_n1EySC8Yg.JPEG.marinblue666%2FIMG_0826.JPG&type=sc960_832'
        urlString3='https://www.shutterstock.com/image-vector/man-holding-megaphone-speech-bubbles-260nw-2079473878.jpg'
        urlString4 = 'https://lib.gwangsan.go.kr/images/ui/sub/facilitystatus/CD/facilitystatus3_1.jpg'
        urlString5 = 'https://lib.gwangsan.go.kr/images/ui/sub/facilitystatus/CD/facilitystatus3_2.jpg'
        urlString6 = 'https://lib.gwangsan.go.kr/images/ui/sub/facilitystatus/CD/facilitystatus3_3.jpg'
        urlString7 = 'https://lib.gwangsan.go.kr/images/ui/sub/facilitystatus/CD/facilitystatus3_4.jpg'
        urlString8 = 'https://lib.gwangsan.go.kr/images/ui/sub/facilitystatus/CD/facilitystatus3_5.jpg'

        imageFromWeb = urllib.request.urlopen(urlString).read()
        imageFromWeb2 = urllib.request.urlopen(urlString2).read()
        imageFromWeb3 = urllib.request.urlopen(urlString3).read()
        imageFromWeb4 = urllib.request.urlopen(urlString4).read()  # 시설이미지
        imageFromWeb5 = urllib.request.urlopen(urlString5).read()
        imageFromWeb6 = urllib.request.urlopen(urlString6).read()
        imageFromWeb7 = urllib.request.urlopen(urlString7).read()
        imageFromWeb8 = urllib.request.urlopen(urlString8).read()

        qPixmapVar = QPixmap()
        qPixmapVar2 = QPixmap()
        qPixmapVar3 = QPixmap()
        qPixmapVar4 = QPixmap()
        qPixmapVar5 = QPixmap()
        qPixmapVar6 = QPixmap()
        qPixmapVar7 = QPixmap()
        qPixmapVar8 = QPixmap()

        qPixmapVar.loadFromData(imageFromWeb)
        qPixmapVar2.loadFromData(imageFromWeb2)
        qPixmapVar3.loadFromData(imageFromWeb3)
        qPixmapVar4.loadFromData(imageFromWeb4)
        qPixmapVar5.loadFromData(imageFromWeb5)
        qPixmapVar6.loadFromData(imageFromWeb6)
        qPixmapVar7.loadFromData(imageFromWeb7)
        qPixmapVar8.loadFromData(imageFromWeb8)

        self.label_pic.setPixmap(qPixmapVar)
        self.main_pic.setPixmap(qPixmapVar2)
        self.event_pic.setPixmap(qPixmapVar3)
        self.label_11.setPixmap(qPixmapVar4)
        self.label_12.setPixmap(qPixmapVar5)
        self.label_13.setPixmap(qPixmapVar6)
        self.label_14.setPixmap(qPixmapVar7)
        self.label_15.setPixmap(qPixmapVar8)
    def txt(self):
        self.label_9.setText("일정 및 행사")
        self.label_2.setText("첨단도서관 [크리스마스랑, 책이랑] 프로그램 안내")
        self.label_3.setText("1인가구를 위한 홈스타일링 강의 안내")
        self.label_4.setText("첨단도서관 시인과 함께하는 힐링인문학")
        self.label_5.setText("첨단도서관 임시 휴관 안내")
        self.label_6.setText("첨단도서관 1인가구 프로그램「나를 돌보는 힐링 드로잉」안내")
        self.label_7.setText("첨단도서관 자기돌봄 글쓰기 프로그램 안내")
        self.label_8.setText("2022년 4분기 독서문화프로그램 홍보 및 모집")
        self.label.setText("            대지	1,500㎡\n\
            건물면적	1,996.79㎡(철근콘크리트 지하1층에서 지상 3층 규모)\n\
            층별안내	\n\
            3층 : 학습실1, 학습실2\n\
            2층 : 종합자료실, 문화교실1, 문화교실2, 시청각실\n\
            1층 : 어린이자료실, • 커뮤니티공간, 사무실\n\
            지하1층 : 전기실")
    def recommend(self):
        f = open('cdan.csv', 'r')
        rdr = csv.reader(f)
        num = random.randrange(1, 48684)
        for line in rdr:
            if line[0] == str(num):
                return line
    def resetb(self):
        self.reco.clear()
        for i in range(0,10):
            self.rebooks=(self.recommend())
            print(self.rebooks[4:7])
            self.reco.insertItem(i,str(self.rebooks[4:7]))
    def login(self):
        print("!!!!!!!!")
        widget.setCurrentIndex(1)
if __name__ == "__main__" :
    # form_class = uic.loadUiType("title.ui")[0]
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    #WindowClass의 인스턴스 생성
    myWindow = FirstClass()
    testlogin = testClass()
    # myWindow.img()
    #프로그램 화면을 보여주는 코드
    widget.addWidget(myWindow)
    widget.addWidget(testlogin)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    # myWindow.show()
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()


