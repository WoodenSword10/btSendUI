import random
import sys
import time
import re
import serial
import serial.tools.list_ports
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import numpy as np
from PyQt5.QtCore import QThread, pyqtSignal, QMutex, Qt, QDateTime, QTimer
import UI_2

# 获取串口数据线程
class Read_data_1(QThread):
    changeforce = pyqtSignal(int, int, int)
    '''
    子进程，用于读取数据
    '''
    def __init__(self):
        super(Read_data_1, self).__init__()
        self.is_open = False
        self.port = serial.Serial()
        self.change = [False, False, False, False, False]


    def change_port(self, port):
        self.port = port
        self.is_open = True
        self.old = np.array(re.findall('\d+', str(self.port.readline()))).astype(int)
        # self.old = np.zeros(5, dtype=int)

    def run(self):
        while True:
            if self.is_open:
                # self.dat
                data = str(self.port.readline())
                # print(data, type(data))
                # print(re.findall('\d+', data))
                self.data = np.array(re.findall('\d+', data))
                self.data = self.data.astype(int)
                # print(self.data)
                for i in range(5):
                    if self.data[i] - self.old[i] > 5:
                        # if not self.change[i]:
                        changevalue = self.data[i] - self.old[i]
                        self.changeforce.emit(0, i, changevalue)
                            # self.change[i] = True
                            # print('5: ' + self.change)
                    elif self.data[i] - self.old[i] < 5:
                        # if self.change[i]:
                        self.changeforce.emit(0, i, 0)
                            # self.change[i] = False
                            # print('5: ' + self.change)
                QThread.msleep(50)
            pass

class Read_data_2(QThread):
    changeforce = pyqtSignal(int, int, int)
    '''
    子进程，用于读取数据
    '''
    def __init__(self):
        super(Read_data_2, self).__init__()
        self.change = [False, False, False, False, False]
        self.port = serial.Serial()
        self.is_open = False

    def change_port(self, port):
        self.port = port
        self.is_open = True
        self.old = np.array(re.findall('\d+', str(self.port.readline()))).astype(int)
        # self.old = np.zeros(5, dtype=int)

    def run(self):
        while True:
            if self.is_open:
                # self.dat
                data = str(self.port.readline())
                # print(data, type(data))
                # print(re.findall('\d+', data))
                self.data = np.array(re.findall('\d+', data))
                self.data = self.data.astype(int)
                # print(self.data)
                for i in range(5):
                    if self.data[i] - self.old[i] > 3:
                        # if not self.change[i]:
                        changevalue = self.data[i] - self.old[i]
                        self.changeforce.emit(1, i, changevalue)
                            # self.change[i] = True
                            # print('5: ' + self.change)
                    elif self.data[i] - self.old[i] < 3:
                        # if self.change[i]:
                        self.changeforce.emit(1, i, 0)
                            # self.change[i] = False
                            # print('5: ' + self.change)
                QThread.msleep(50)
            pass

class Read_data_3(QThread):
    changeforce = pyqtSignal(int, int, int)
    '''
    子进程，用于读取数据
    '''
    def __init__(self):
        super(Read_data_3, self).__init__()
        self.change = [False, False, False, False, False]
        self.port = serial.Serial()
        self.is_open = False

    def change_port(self, port):
        self.port = port
        self.is_open = True
        self.old = np.array(re.findall('\d+', str(self.port.readline()))).astype(int)
        # self.old = np.zeros(5, dtype=int)

    def run(self):
        while True:
            if self.is_open:
                # self.dat
                data = str(self.port.readline())
                # print(data, type(data))
                # print(re.findall('\d+', data))
                self.data = np.array(re.findall('\d+', data))
                self.data = self.data.astype(int)
                # print(self.data)
                for i in range(5):
                    if  i == 1:
                        if self.data[1] - self.old[1] > 1:
                            changevalue = self.data[i] - self.old[i]
                            self.changeforce.emit(2, 1, changevalue)
                        else:
                            self.changeforce.emit(2, 1, 0)
                    if  i == 4:
                        if self.data[4] - self.old[4] > 200:
                            changevalue = self.data[i] - self.old[i]
                            self.changeforce.emit(2, 4, changevalue)
                        else:
                            self.changeforce.emit(2, 4, 0)
                    if self.data[i] - self.old[i] > 20:
                        # if not self.change[i]:
                        changevalue = self.data[i] - self.old[i]
                        self.changeforce.emit(2, i, changevalue)
                            # self.change[i] = True
                            # print('5: ' + self.change)
                    elif self.data[i] - self.old[i] < 20:
                        # if self.change[i]:
                        self.changeforce.emit(2, i, 0)
                            # self.change[i] = False
                            # print('5: ' + self.change)
                QThread.msleep(50)
            pass

class Read_data_4(QThread):
    changeforce = pyqtSignal(int, int, int)
    '''
    子进程，用于读取数据
    '''
    def __init__(self):
        super(Read_data_4, self).__init__()
        self.change = [False, False, False, False, False]
        self.port = serial.Serial()
        self.is_open = False

    def change_port(self, port):
        self.port = port
        self.is_open = True
        self.old = np.array(re.findall('\d+', str(self.port.readline()))).astype(int)
        # self.old = np.zeros(5, dtype=int)

    def run(self):
        while True:
            if self.is_open:
                # self.dat
                data = str(self.port.readline())
                # print(data, type(data))
                # print(re.findall('\d+', data))
                self.data = np.array(re.findall('\d+', data))
                self.data = self.data.astype(int)
                # print(self.data)
                for i in range(5):
                    if self.data[i] - self.old[i] > 15:
                        # if not self.change[i]:
                        changevalue = self.data[i] - self.old[i]
                        self.changeforce.emit(3, i, changevalue)
                            # self.change[i] = True
                            # print('5: ' + self.change)
                    elif self.data[i] - self.old[i] < 15:
                        # if self.change[i]:
                        self.changeforce.emit(3, i, 0)
                            # self.change[i] = False
                            # print('5: ' + self.change)
                QThread.msleep(50)
            pass

class Read_data_5(QThread):
    changeforce = pyqtSignal(int, int, int)
    '''
    子进程，用于读取数据
    '''
    def __init__(self):
        super(Read_data_5, self).__init__()
        self.change = [False, False, False, False, False]
        self.port = serial.Serial()
        self.is_open = False

    def change_port(self, port):
        self.port = port
        self.is_open = True
        self.old = np.array(re.findall('\d+', str(self.port.readline()))).astype(int)
        # self.old = np.zeros(5, dtype=int)

    def run(self):
        while True:
            if self.is_open:
                # self.dat
                data = str(self.port.readline())
                # print(data, type(data))
                # print(re.findall('\d+', data))
                self.data = np.array(re.findall('\d+', data))
                self.data = self.data.astype(int)
                # print(self.data)
                for i in range(5):
                    if self.data[i] - self.old[i] > 15:
                        # if not self.change[i]:
                        changevalue = self.data[i] - self.old[i]
                        self.changeforce.emit(4, i, changevalue)
                            # self.change[i] = True
                            # print('5: ' + self.change)
                    elif self.data[i] - self.old[i] < 15:
                        # if self.change[i]:
                        self.changeforce.emit(4, i, 0)
                            # self.change[i] = False
                            # print('5: ' + self.change)
                QThread.msleep(50)
            pass

class Find_port(QThread):
    '''
    寻找存在的串口
    '''
    # 串口改变信号
    port_change = pyqtSignal()

    def __init__(self):
        super(Find_port, self).__init__()
        # 获取初始串口列表
        self.old = list(serial.tools.list_ports.comports())

    def run(self):
        while True:
            # 再次获取串口列表
            port_list = list(serial.tools.list_ports.comports())
            # 如果串口列表发生了变化
            if port_list != self.old:
                # 更改初始串口列表
                self.old = port_list
                # 发出信号
                self.port_change.emit()
                # 强制休息1000毫秒
                QThread.msleep(1000)

class Main_window(QMainWindow, UI_2.Ui_Dialog):

    def __init__(self, parent=None):
        # 窗口初始化
        super(Main_window, self).__init__(parent)
        self.setupUi(self)
        # 实例化端口号变化线程
        self.thread = Find_port()
        # 线程内置串口改变信号链接函数
        self.thread.port_change.connect(self.port_find)
        # 启动线程
        self.thread.start()
        self.thread1 = Read_data_1()
        self.thread2 = Read_data_2()
        self.thread3 = Read_data_3()
        self.thread4 = Read_data_4()
        self.thread5 = Read_data_5()
        self.thread1.changeforce.connect(self.form_data)
        self.thread2.changeforce.connect(self.form_data)
        self.thread3.changeforce.connect(self.form_data)
        self.thread4.changeforce.connect(self.form_data)
        self.thread5.changeforce.connect(self.form_data)
        # 数据
        self.data = np.zeros([5, 5])
        self.old_dat = ''
        # 波特率列表设置
        self.bote_list = ['9600', '115200']
        # 填充复选框内容
        self.comboBox_2.addItems(self.bote_list)
        self.comboBox_4.addItems(self.bote_list)
        self.comboBox_6.addItems(self.bote_list)
        self.comboBox_8.addItems(self.bote_list)
        self.comboBox_10.addItems(self.bote_list)
        self.comboBox_12.addItems(self.bote_list)
        # 用于存放处理后串口列表
        list1 = []
        # 获取串口列表
        self.port_list = list(serial.tools.list_ports.comports())
        # 对串口列表进行处理，仅保留COMxx
        for item in self.port_list:
            # 使用正则匹配
            pattern = re.compile('COM[\d]*')
            # 找出符号要求的字符串
            item = pattern.findall(str(item))[0]
            # 添加入列表中
            list1.append(item)
        # 对列表进行排序
        list1.sort()
        # 填充复选框内容
        self.comboBox.addItems(list1)
        self.comboBox_3.addItems(list1)
        self.comboBox_5.addItems(list1)
        self.comboBox_7.addItems(list1)
        self.comboBox_9.addItems(list1)
        self.comboBox_11.addItems(list1)
        # 按钮点击事件
        self.pushButton.clicked.connect(self.port_connect)
        self.pushButton_2.clicked.connect(self.send_cs)
        self.pushButton_3.clicked.connect(self.clear_content)
        self.textBrowser.insertPlainText("测试")
        self.t = QTimer()
        self.t.timeout.connect(self.send_timer)

    def send_timer(self):
        dat = str(int(self.data[0][0])) + '-' + str(int(self.data[0][1])) + '-' + str(int(self.data[0][2])) + '-' + str(
            int(self.data[0][3])) + '-' + str(int(self.data[0][4])) + '-' + str(int(self.data[1][0])) + '-' + str(
            int(self.data[1][1])) + '-' + str(int(self.data[1][2])) + '-' + str(int(self.data[1][3])) + '-' + str(
            int(self.data[1][4])) + '-' + str(int(self.data[2][0])) + '-' + str(int(self.data[2][1])) + '-' + str(
            int(self.data[2][2])) + '-' + str(int(self.data[2][3])) + '-' + str(int(self.data[2][4])) + '-' + str(
            int(self.data[3][0])) + '-' + str(int(self.data[3][1])) + '-' + str(int(self.data[3][2])) + '-' + str(
            int(self.data[3][3])) + '-' + str(int(self.data[3][4])) + '-' + str(int(self.data[4][0])) + '-' + str(
            int(self.data[4][1])) + '-' + str(int(self.data[4][2])) + '-' + str(int(self.data[4][3])) + '-' + str(
            int(self.data[4][4]))

        if dat == self.old_dat:
            pass
        else:
            try:
                self.port6.write(dat.encode())
            except Exception as e:
                pass
            else:
                self.textBrowser.insertPlainText("发送数据：\n" + dat + '\n')
                self.old_dat = dat

    def send_cs(self):
        # box = QMessageBox()
        dat = str(int(self.data[0][0])) + '-' + str(int(self.data[0][1])) + '-' + str(int(self.data[0][2])) + '-' + str(
            int(self.data[0][3])) + '-' + str(int(self.data[0][4])) + '-' + str(int(self.data[1][0])) + '-' + str(
            int(self.data[1][1])) + '-' + str(int(self.data[1][2])) + '-' + str(int(self.data[1][3])) + '-' + str(
            int(self.data[1][4])) + '-' + str(int(self.data[2][0])) + '-' + str(int(self.data[2][1])) + '-' + str(
            int(self.data[2][2])) + '-' + str(int(self.data[2][3])) + '-' + str(int(self.data[2][4])) + '-' + str(
            int(self.data[3][0])) + '-' + str(int(self.data[3][1])) + '-' + str(int(self.data[3][2])) + '-' + str(
            int(self.data[3][3])) + '-' + str(int(self.data[3][4])) + '-' + str(int(self.data[4][0])) + '-' + str(
            int(self.data[4][1])) + '-' + str(int(self.data[4][2])) + '-' + str(int(self.data[4][3])) + '-' + str(
            int(self.data[4][4]))
        self.textBrowser.insertPlainText("发送数据：\n" + dat + '\n')
        # try:
        #     self.port6.write(dat.encode())
        # except Exception as e:
        #     box.setText('<h1>尚未连接！！</h1>')
        # else:
        #     box.setText('<h1>发送成功！！'+ dat + '</h1>')
        # box.exec_()



    def clear_content(self):
        self.textBrowser.clear()

    # 串口刷新显示函数
    def port_find(self):
        '''
        定时刷新显示串口列表
        :return:
        '''
        # 清空两个复选框
        self.comboBox.clear()
        self.comboBox_3.clear()
        self.comboBox_5.clear()
        self.comboBox_7.clear()
        self.comboBox_9.clear()
        self.comboBox_11.clear()
        # 用于存放处理后串口列表
        list1 = []
        # 获取串口列表
        self.port_list = list(serial.tools.list_ports.comports())
        # 对串口列表进行处理，仅保留COMxx
        for item in self.port_list:
            # 使用正则匹配
            pattern = re.compile('COM[\d]*')
            # 找出符号要求的字符串
            item = pattern.findall(str(item))[0]
            # 添加入列表中
            list1.append(item)
        # 对列表进行排序
        list1.sort()
        # 填充复选框内容
        self.comboBox.addItems(list1)
        self.comboBox_3.addItems(list1)
        self.comboBox_5.addItems(list1)
        self.comboBox_7.addItems(list1)
        self.comboBox_9.addItems(list1)
        self.comboBox_11.addItems(list1)

    # 串口连接函数
    def port_connect(self):
        box = QMessageBox()
        try:
            self.port1 = serial.Serial(self.comboBox.currentText(), self.comboBox_2.currentText())
            self.port2 = serial.Serial(self.comboBox_3.currentText(), self.comboBox_4.currentText())
            self.port3 = serial.Serial(self.comboBox_5.currentText(), self.comboBox_6.currentText())
            self.port4 = serial.Serial(self.comboBox_7.currentText(), self.comboBox_8.currentText())
            self.port5 = serial.Serial(self.comboBox_9.currentText(), self.comboBox_10.currentText())
            self.port6 = serial.Serial(self.comboBox_11.currentText(), self.comboBox_12.currentText())
        except:
            box.setText("<h1>连接失败！！</h1>")
        else:
            self.thread1.change_port(self.port1)
            self.thread2.change_port(self.port2)
            self.thread3.change_port(self.port3)
            self.thread4.change_port(self.port4)
            self.thread5.change_port(self.port5)
            self.thread1.start()
            self.thread2.start()
            self.thread3.start()
            self.thread4.start()
            self.thread5.start()
            self.t.start(1000)
            box.setText("<h1>连接成功！！</h1>")
        box.exec_()

    def form_data(self, a, b, c):
        self.data[a][b] = c
        # dat = str(int(self.data[0][0])) + '-' + str(int(self.data[0][1])) + '-' + str(int(self.data[0][2])) + '-' + str(int(self.data[0][3])) + '-' + str(int(self.data[0][4])) + '-' + str(int(self.data[1][0])) + '-' + str(int(self.data[1][1])) + '-' + str(int(self.data[1][2])) + '-' + str(int(self.data[1][3])) + '-' + str(int(self.data[1][4])) + '-' + str(int(self.data[2][0])) + '-' + str(int(self.data[2][1])) + '-' + str(int(self.data[2][2])) + '-' + str(int(self.data[2][3])) + '-' + str(int(self.data[2][4])) + '-' + str(int(self.data[3][0])) + '-' + str(int(self.data[3][1])) + '-' + str(int(self.data[3][2])) + '-' + str(int(self.data[3][3])) + '-' + str(int(self.data[3][4])) + '-' + str(int(self.data[4][0])) + '-' + str(int(self.data[4][1])) + '-' + str(int(self.data[4][2])) + '-' + str(int(self.data[4][3])) + '-' + str(int(self.data[4][4]))
        # self.textBrowser.insertPlainText("发送数据：\n" + dat + '\n')
        # self.port6.write(dat.encode())


if __name__ == '__main__':
    # 实现不同分辨率下的电脑上的相同显示
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    beginWin = Main_window()
    beginWin.show()
    sys.exit(app.exec_())