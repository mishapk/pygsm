#!-*-coding:utf-8-*-
import pyaudio
import wave
import audioop, numpy, struct, math,time
import os
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic, QtCore, QtSql
class GSM_list1(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        layout = QVBoxLayout(self)
        table = QTableWidget()
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(['Модем','Состояние','C','A','D',''])
        table.setColumnWidth(0,60)
        table.setColumnWidth(1,120)
        table.setColumnWidth(2,20)
        table.setColumnWidth(3,20)
        table.setColumnWidth(4,20)
        table.setColumnWidth(5,30)
        n=24
        table.setRowCount(n)
        for i in range(n):
            button = QToolButton()
            button.setText('...')
            table.setCellWidget(i,5,button)
            table.setItem(i,0,QTableWidgetItem('SIM{}'.format(i)))
            table.setItem(i,1,QTableWidgetItem('Идет дозвон: +38097846xxxx'))
            r1 = QRoundWidget(0,0,20)
            r2 = QRoundWidget(0,0,20)
            r3 = QRoundWidget(0,0,20)
            table.setCellWidget(i,2,r1)
            table.setCellWidget(i,3,r2)
            table.setCellWidget(i,4,r3)
        layout.addWidget(table)
class GSM_list(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self, parent)
        widget = QWidget()
        gb=QVBoxLayout()
        gb.setSpacing(0)
        n=64
        for i in range(n):
            gi=GSM_item()
            gb.addWidget(gi)
            gi.setName('GSM{}'.format(i))
        widget.setLayout(gb)
        sa= QScrollArea(self)
        sa.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        sa.setWidgetResizable(False)
        sa.setWidget(widget)

class GSM_item(QFrame):
    def __init__(self,parent=None):
        QFrame.__init__(self, parent)
        self.initGraphic()
    def setName(self,text):
        self.LabelName.setText(text)
        self.setFrameShape(QFrame.StyledPanel)

    def initGraphic(self):
        gb=QHBoxLayout(self)
        self.r1=QRoundWidget(0,0,20)
        self.r2=QRoundWidget(0,0,20)
        self.r3=QRoundWidget(0,0,20)
        self.LabelName=QLabel('GSM88')
        self.LabelName.setFixedSize(60,20)
        self.LabelInfo=QLabel('Набор номера:\n+38098846996')
        self.LabelInfo.setFixedSize(120,30)
        button = QToolButton()
        button.setText('...')

        gb.addWidget(self.LabelName)
        gb.addWidget(self.LabelInfo)
        gb.addWidget(self.r1)
        gb.addWidget(self.r2)
        gb.addWidget(self.r3)
        gb.addWidget(button)
        #self.setFixedSize(300,40)
        #self.setContentsMargins(QMargins(0,0,0,0))

class QRoundWidget(QWidget):
    def __init__(self, x,y,r,parent=None):
        QWidget.__init__(self, parent)
        self.x=x
        self.y=y
        self.r=r
        self.setFixedSize(r,r)

    def paintEvent(self,e):
        painter= QPainter(self)
        painter.setBrush(Qt.red)
        k=1.5
        painter.drawEllipse(self.x,self.y, self.r/k,self.r/k)
        QWidget.paintEvent(self,e)





