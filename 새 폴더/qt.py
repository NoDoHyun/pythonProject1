import sys
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QStackedWidget, QPushButton, QLabel, QDialog, \
    QApplication
from PyQt5.QtGui import QPixmap


class MainDialog(QDialog):
    def __init__(self):
        super().__init__()

        vertical_layout = QVBoxLayout()         #qvbox=수직방향,위에서 아래로 위젯을 배치할때사용,그래서 버티컬 레이아웃이라는 이름을줌

        stack1 = QWidget()                      #qwidget은 창을생성한다,페이지 두개 만들어야 하기때문에 두개의 스택으로 받았다
        stack2 = QWidget()

        self.Stack = QStackedWidget()           #self.stack을 qstackedwidget으로 선언
        self.Stack.addWidget(stack1)            #addwidget을 위에 선언한 스택을인자로 불러서 qstackedwidget 객체에 추가
        self.Stack.addWidget(stack2)            #addwidget을 위에 선언한 스택을인자로 불러서 qstackedwidget 객체에 추가

        horizontal_layout1 = QHBoxLayout()      #qvbox와 반대, v=vertical, h=horizontal
        label1 = QLabel()
        label2 = QLabel()
        horizontal_layout1.addWidget(label1)
        horizontal_layout1.addWidget(label2)
        pixmap = QPixmap('images.jpg')
        pixmap2 = QPixmap('snowfox.jpg')
        label1.setPixmap(pixmap)
        label2.setPixmap(pixmap2)

        stack1.setLayout(horizontal_layout1)

        horizontal_layout2 = QHBoxLayout(self)
        label3 = QLabel()
        horizontal_layout2.addWidget(label3)
        label3.setPixmap(pixmap)
        label3.setScaledContents(True)
        stack2.setLayout(horizontal_layout2)

        vertical_layout.addWidget(self.Stack)

        horizontal_layout3 = QHBoxLayout()
        self.Button1 = QPushButton('STACK 1', self)
        self.Button1.clicked.connect(self.show_stack1)
        self.Button2 = QPushButton('STACK 2', self)
        self.Button2.clicked.connect(self.show_stack2)
        horizontal_layout3.addWidget(self.Button1)
        horizontal_layout3.addWidget(self.Button2)

        vertical_layout.addLayout(horizontal_layout3)

        self.setLayout(vertical_layout)

        self.Button1.setEnabled(False)

    def show_stack1(self):
        self.Stack.setCurrentIndex(0)
        self.Button1.setEnabled(False)
        self.Button2.setEnabled(True)

    def show_stack2(self):
        self.Stack.setCurrentIndex(1)
        self.Button1.setEnabled(True)
        self.Button2.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    dlg = MainDialog()

    dlg.show()
    app.exec_()