import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import csv

# 09 40 엔터 기능 추가
# 10 10 대여 가능 여부 출력 오류 수정
# 12 10 대여 기능의 정확성을 위해 기준을 등록번호로 수정
# 13 40 팀원들의 진행 상황을 확인하기 위해 회의 진행
# 14 15 대여 가능 여부가 여러 번 출력되는 것을 수정
# 15 50 출력 양식을 수정

# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("lib_2.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class SearchBookInfo(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Search.clicked.connect(self.search)
        self.Find.returnPressed.connect(self.search)
        self.pushButton.clicked.connect(self.move_main)

    def search(self):
        book_info_s = open("singa.csv", 'r')
        books_s = list(csv.reader(book_info_s))
        book_info_j = open("jangduk.csv", 'r')
        books_j = list(csv.reader(book_info_j))
        book_info_c = open("cdan.csv", 'r')
        books_c = list(csv.reader(book_info_c))
        book_info_e = open("flower.csv", 'r')
        books_e = list(csv.reader(book_info_e))
        rent_info = open("RentInfo.csv")
        rented = list(csv.reader(rent_info))
        self.Found.clear()
        for i in range(len(books_s)):
            if self.Find.text() in books_s[i][4] or self.Find.text() in books_s[i][3]:
                self.Found.append(str(books_s[i]))
                for j in range(len(rented)):
                    if books_s[i][3] in rented[j][0]:
                        self.Found.append(" - (대여 중, 7일 후 반납)")
                        break
                    else:
                        if j == len(rented) - 1:
                            self.Found.append(" - (대여 가능)")
                        continue
        for i in range(len(books_j)):
            if self.Find.text() in books_j[i][4] or self.Find.text() in books_j[i][3]:
                self.Found.append(str(books_j[i]))
                for j in range(len(rented)):
                    if books_j[i][3] in rented[j][0]:
                        self.Found.append(" - (대여 중, 7일 후 반납)")
                        break
                    else:
                        if j == len(rented) - 1:
                            self.Found.append(" - (대여 가능)")
                        continue
        for i in range(len(books_c)):
            if self.Find.text() in books_c[i][4] or self.Find.text() in books_c[i][3]:
                self.Found.append(str(books_c[i]))
                for j in range(len(rented)):
                    if books_c[i][3] in rented[j][0]:
                        self.Found.append(" - (대여 중, 7일 후 반납)")
                        break
                    else:
                        if j == len(rented) - 1:
                            self.Found.append(" - (대여 가능)")
                        continue
        for i in range(len(books_e)):
            if self.Find.text() in books_e[i][4] or self.Find.text() in books_e[i][3]:
                self.Found.append(str(books_e[i]))
                for j in range(len(rented)):
                    if books_e[i][3] in rented[j][0]:
                        self.Found.append(" - (대여 중, 7일 후 반납)")
                        break
                    else:
                        if j == len(rented) - 1:
                            self.Found.append(" - (대여 가능)")
                        continue

    def move_main(self):
        self.parent().setCurrentIndex(0)


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = SearchBookInfo()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
