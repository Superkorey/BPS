# ！usr/python/env python
# _*_ codeing: UTF-8 _*_
__Author__ = "Create by korey 2021/3/29"
"""
CC PTS converter to ACCO PGS
ACCO PGS converter to CC PTS
"""

from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from win32api import GetSystemMetrics
import qtawesome


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        #设置主登录窗口的标题
        self.setWindowTitle("BPS")
        # 获取主屏幕尺寸
        sceenwidth = GetSystemMetrics(0)
        sceenheight = GetSystemMetrics(1)
        self.resize(int(sceenwidth*0.7),int(sceenheight*0.7))
        #设置窗口在屏幕中间
        self.move(int(sceenwidth*0.15),int(sceenheight*0.1))
        #主界面布局
        vlayout = QHBoxLayout()
        vlayout.setContentsMargins(0,0,0,0)

        #左边功能区
        leftsidewg = QWidget()
        leftsidewg.setFixedWidth(50)
        leftsidewg.setStyleSheet("background-color:#3A3838")

        #添加功能按钮
        leftsidelayout = QVBoxLayout()

        fileconventertbn = QPushButton(qtawesome.icon('fa.plus',color='white'),None)
        fileconventertbn.setStyleSheet("border:#3A3838")

        dataanalysisbtn = QPushButton(qtawesome.icon('fa.bar-chart', color='white'), None)
        dataanalysisbtn.setStyleSheet("border:#3A3838")

        peoplebtn = QPushButton(qtawesome.icon('fa.reddit', color='white'), None)
        peoplebtn.setStyleSheet("border:#3A3838")

        setting = QPushButton(qtawesome.icon('fa.gear', color='white'), None)
        setting.setStyleSheet("border:#3A3838")

        leftsidelayout.addWidget(fileconventertbn)
        leftsidelayout.addWidget(peoplebtn)
        leftsidelayout.addWidget(dataanalysisbtn)
        leftsidelayout.addWidget(setting)

        leftsidewg.setLayout(leftsidelayout)

        #右边试图区
        rightsidewg = QWidget()


        vlayout.addWidget(leftsidewg)
        vlayout.addWidget(rightsidewg)

        self.setLayout(vlayout)


        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

    #111