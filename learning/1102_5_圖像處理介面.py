import sys
import cv2
import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class winForm(QMainWindow):
    def __init__(self,parent=None):   #__init__ 等同建構子
        super(winForm,self).__init__(parent)
        self.setGeometry(400,150,1738,799)   #視窗起始位置大小
        layout=QVBoxLayout()
        self.btnl=QPushButton('開啟圖片',self)
        self.btnl.setGeometry(10,10,60,30) #按鈕位置大小
        self.btnl.clicked.connect(self.open)

        self.btnl=QPushButton('關閉視窗',self)
        self.btnl.setGeometry(1320,10,60,30) 
        self.btnl.clicked.connect(self.close)

        self.btnl=QPushButton('存檔',self)
        self.btnl.setGeometry(1250,10,60,30) 
        self.btnl.clicked.connect(self.save)

        self.btnl=QPushButton('HSV',self)
        self.btnl.setGeometry(80,10,60,30) 
        self.btnl.clicked.connect(self.HSV)

        self.btnl=QPushButton('模糊',self)
        self.btnl.setGeometry(150,10,60,30) 
        self.btnl.clicked.connect(self.blurre)

        self.btnl=QPushButton('灰階',self)
        self.btnl.setGeometry(220,10,60,30) 
        self.btnl.clicked.connect(self.gray)

        self.btnl=QPushButton('二值化',self)
        self.btnl.setGeometry(290,10,60,30)
        self.btnl.clicked.connect(self.canny)

        self.btnl=QPushButton('膨脹',self)
        self.btnl.setGeometry(360,10,60,30)
        self.btnl.clicked.connect(self.dilated)

        self.btnl=QPushButton('侵蝕',self)
        self.btnl.setGeometry(430,10,60,30)
        self.btnl.clicked.connect(self.eroded)

        self.btnl=QPushButton('高倍偵測',self)
        self.btnl.setGeometry(500,10,60,30)
        self.btnl.clicked.connect(self.circle)

        self.btnl=QPushButton('低倍偵測',self)
        self.btnl.setGeometry(570,10,60,30)
        self.btnl.clicked.connect(self.circle1)

        self.label=QLabel('',self)
        self.label.setGeometry(10,45,554,739)
        layout.addWidget(self.label)
        
        self.label2=QLabel('',self)
        self.label2.setGeometry(574,45,554,739)
        layout.addWidget(self.label2)
        
        self.setLayout(layout)
        self.setWindowTitle('opencv圖像處理')
    
    def Show(self):  
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        self.label.setPixmap (QPixmap(self.qImg))
        self.label.setScaledContents (True)
        
    def refreshShow(self):
        height, width, channel = self.img.shape
        bytesPerLine = 3 * width
        self.qImg = QImage(self.img.data, width, height, bytesPerLine,
                           QImage.Format_RGB888).rgbSwapped()
        self.label2.setPixmap (QPixmap(self.qImg))
        self.label2.setScaledContents (True)
        
    def GRAYrefreshShow(self):
        height, width = self.img.shape
        self.qImg = QImage(self.img.data, width, height,width, 
                            QImage.Format_Grayscale8)
        self.label2.setPixmap(QPixmap.fromImage(self.qImg))
        self.label2.setScaledContents (True)

    def open(self):
        File,_=QFileDialog.getOpenFileName(self,'Open File','c:\\','Image File(*.jpg *jpeg *.png)')
        if File is '':
            return        #return 沒有接東西就是回傳None, 但寫return相當於結束方法,後續程式不會執行
        self.img=cv2.imread(File,-1)
        if self.img.size==1:
            return
        self.Show()
        self.refreshShow()

    def close(self):
        pass
    def save(self):
        pass
    def HSV(self):
        pass
    def blurre(self):
        if self.img.size==1:
            return
        self.img=cv2.GaussianBlur(self.img,(9,9),0)   #高斯模糊
        self.refreshShow()

    def gray(self):
        pass
    def canny(self):
        pass
    def dilated(self):
        pass
    def eroded(self):
        pass
    def circle(self):
        pass
    def circle1(self):
        pass

if __name__=='__main__':
    app=QApplication(sys.argv)
    win=winForm()      #實體化介面
    win.show()         #實體化介面
    sys.exit(app.exec_())    #右上角'X'可關閉

