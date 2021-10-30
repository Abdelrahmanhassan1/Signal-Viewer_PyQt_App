# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\IsaWorking-Copy.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
from matplotlib.animation import FuncAnimation
import numpy as np
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1182, 888)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 80, 1081, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1077, 147))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 50, 101, 31))
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 50, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(380, 20, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 50, 101, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 20, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(710, 50, 93, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(480, 20, 101, 31))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(480, 50, 101, 31))
        self.pushButton_20.setObjectName("pushButton_20")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(130, 50, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(590, 51, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 580, 1081, 201))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(220, 800, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(710, 800, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 560, 121, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 550, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(810, 50, 101, 31))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 550, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(480, 540, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(810, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 230, 1081, 151))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.verticalLayoutWidget_3)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 1077, 147))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.addWidget(self.scrollArea_2)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 380, 1081, 151))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.verticalLayoutWidget_4)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1077, 147))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_5.addWidget(self.scrollArea_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(920, 20, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(920, 50, 121, 31))
        self.comboBox_4.setObjectName("comboBox_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(1050, 20, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(1050, 50, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setGeometry(QtCore.QRect(640, 560, 131, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 540, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(650, 540, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1182, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##########################################################
        self.min_slider = 0
        self.avg_slider = (1999 - 1) // 2
        self.max_slider = 1999
        self.speed = 10
        self.status_1 = True
        self.status_2 = True
        self.status_3 = True


        self.pallete = "viridis"
        self.combo_items_4 = ["plasma", "rainbow", "inferno", "magma", "viridis"]
        self.comboBox_5.addItems(self.combo_items_4)

        self.combo_items = ["channel_1", "channel_2", "channel_3"]
        self.comboBox.addItems(self.combo_items)
        self.comboBox_2.addItems(self.combo_items)

        self.selected_color = "grey"
        self.combo_items_2 = ["black", "red", "orange", "green", "blue", "grey"]
        self.comboBox_3.addItems(self.combo_items_2)

        self.selected_theme = "default"
        self.combo_items_3 = ["default", "fivethirtyeight", "bmh"]
        self.comboBox_4.addItems(self.combo_items_3)

        self.figureemg_1 = Figure()
        self.canvasemg_1 = FigureCanvas(self.figureemg_1)
        self.scrollArea.setWidget(self.canvasemg_1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.verticalLayout.addWidget(self.scrollArea)


        self.figureemg_2 = Figure()
        self.canvasemg_2 = FigureCanvas(self.figureemg_2)
        self.scrollArea_2.setWidget(self.canvasemg_2)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.verticalLayout_3.addWidget(self.scrollArea_2)

        self.figureemg_3 = Figure()
        self.canvasemg_3 = FigureCanvas(self.figureemg_3)
        self.scrollArea_3.setWidget(self.canvasemg_3)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(True)
        self.verticalLayout_5.addWidget(self.scrollArea_3)

        self.figure_2 = Figure()
        self.figure_canvas_2 = FigureCanvas(self.figure_2)
        self.verticalLayout_2.addWidget(self.figure_canvas_2)


        self.first_col_1 = []
        self.second_col_1 = []

        self.first_col_2 = []
        self.second_col_2 = []

        self.first_col_3 = []
        self.second_col_3 = []

        self.horizontalSlider.setMinimum(self.min_slider)
        self.horizontalSlider.setMaximum(self.avg_slider - 1)

        self.horizontalSlider_2.setMinimum(self.avg_slider + 1)
        self.horizontalSlider_2.setMaximum(self.max_slider)

        self.pushButton.clicked.connect(self.import_csv)
        self.pushButton_2.clicked.connect(self.playback)
        self.pushButton_4.clicked.connect(self.zoom_in)
        self.pushButton_5.clicked.connect(self.zoom_out)
        self.pushButton_3.clicked.connect(self.add_label)
        self.pushButton_7.clicked.connect(self.spectrogram)
        self.pushButton_19.clicked.connect(self.increase_speed)
        self.pushButton_20.clicked.connect(self.decrease_speed)
        self.pushButton_10.clicked.connect(self.hide_signal)
        self.pushButton_9.clicked.connect(self.show_signal)
        self.pushButton_6.clicked.connect(lambda: self.save_figure("Signals", 1))
        self.pushButton_8.clicked.connect(lambda: self.save_figure("Spectrogram", 2))

    def import_csv(self):
        try:
            self.fileName = QFileDialog.getOpenFileName(filter="CSV (*.csv)")[0]
            data_frame = pd.read_csv(self.fileName)
            channel = self.comboBox.currentIndex()
            if channel == 0:
                self.first_col_1 = data_frame.iloc[:, 0].values
                print(self.first_col_1)
                self.second_col_1 = data_frame.iloc[:, 1].values
                self.frame_counter_img_1 = 100
                self.flag_img_1 = False
            elif channel == 1:
                self.first_col_2 = data_frame.iloc[:, 0].values
                print(self.first_col_1)
                self.second_col_2 = data_frame.iloc[:, 1].values
                self.frame_counter_img_2 = 100
                self.flag_img_2 = False
            elif channel == 2:
                self.first_col_3 = data_frame.iloc[:, 0].values
                print(self.first_col_1)
                self.second_col_3 = data_frame.iloc[:, 1].values
                self.frame_counter_img_3 = 100
                self.flag_img_3 = False
        except Exception as e:
            print(e)

    def playback(self):
        try:
            channel = self.comboBox.currentIndex()
            if channel == 0:
                self.playBack_1()
            elif channel == 1:
                self.playBack_2()
            elif channel == 2:
                self.playBack_3()
        except Exception as e:
            print(e)

    def playBack_1(self):
        try:
            if not self.flag_img_1:
                self.flag_img_1 = True
                c = self.frame_counter_img_1
                self.figureemg_1.clear()
                lines = [ax.plot([], [])[0] for ax in self.figureemg_1.axes]

                def update(i):
                    if not self.flag_img_1:
                        self.ani_emg_1.event_source.stop()
                        self.canvasemg_1.flush_events()
                    else:
                        # To change color:
                        self.change_color()
                        # To change theme:
                        self.change_theme()
                        plt.style.use(self.selected_theme)
                        ###############
                        self.frame_counter_img_1 = i + c
                        range_min_1 = 2 * int(((self.frame_counter_img_1 - 100) + abs(self.frame_counter_img_1 - 100))/2)
                        x_axis_1 = self.first_col_1[range_min_1:2 * self.frame_counter_img_1]
                        y_axis_1 = self.second_col_1[range_min_1:2 * self.frame_counter_img_1]
                        ax_1 = self.figureemg_1.gca()
                        # Show or hide
                        ax_1.set_visible(self.status_1)
                        ################
                        ax_1.cla()
                        ax_1.axes.get_xaxis().set_visible(False)
                        ax_1.spines[["right", "bottom", "top"]].set_visible(False)
                        ax_1.set_ylim(min(self.second_col_1) - 0.5, max(self.second_col_1) + 0.5)
                        # ax_1.set_facecolor((1, 1, 1))
                        # ax_1.grid(True)
                        ax_1.plot(x_axis_1, y_axis_1, color=self.selected_color)
                        self.canvasemg_1.draw()
                    self.canvasemg_1.flush_events()
                    return lines
                self.ani_emg_1 = FuncAnimation(self.figureemg_1, update,
                                               frames=100,
                                               interval=self.speed, blit=True)
            else:
                self.flag_img_1 = False
        except Exception as e:
            print(e)

    def playBack_2(self):
        try:
            if not self.flag_img_2:
                self.flag_img_2 = True
                c = self.frame_counter_img_2
                self.figureemg_2.clear()
                lines = [ax.plot([], [])[0] for ax in self.figureemg_2.axes]

                def update(i):
                    if not self.flag_img_2:
                        self.ani_img_2.event_source.stop()
                        self.canvasemg_2.flush_events()
                    else:
                        # To change color:
                        self.change_color()
                        # To change theme:
                        self.change_theme()
                        plt.style.use(self.selected_theme)

                        self.frame_counter_img_2 = i + c
                        range_min_2 = 2 * int(((self.frame_counter_img_2 - 100) + abs(self.frame_counter_img_2 - 100)) / 2)
                        x_axis_2 = self.first_col_2[range_min_2:2 * self.frame_counter_img_2]
                        y_axis_2 = self.second_col_2[range_min_2:2 * self.frame_counter_img_2]
                        ax_2 = self.figureemg_2.gca()

                        ax_2.set_visible(self.status_2)

                        ax_2.cla()
                        ax_2.axes.get_xaxis().set_visible(False)
                        ax_2.spines[["right", "bottom", "top"]].set_visible(False)
                        ax_2.set_ylim(min(self.second_col_2) - 0.5, max(self.second_col_2) + 0.5)
                        ax_2.set_facecolor((1, 1, 1))
                        ax_2.grid(True)
                        ax_2.plot(x_axis_2, y_axis_2, color=self.selected_color)
                        self.canvasemg_2.draw()
                    self.canvasemg_2.flush_events()
                    return lines

                self.ani_img_2 = FuncAnimation(self.figureemg_2, update,
                                               frames=100,
                                               interval=self.speed, blit=True)
            else:
                self.flag_img_2 = False
        except Exception as e:
            print(e)

    def playBack_3(self):
        try:
            if not self.flag_img_3:
                self.flag_img_3 = True
                c = self.frame_counter_img_3
                self.figureemg_3.clear()
                lines = [ax.plot([], [])[0] for ax in self.figureemg_3.axes]

                def update(i):
                    if not self.flag_img_3:
                        self.ani_img_3.event_source.stop()
                        self.canvasemg_3.flush_events()
                    else:
                        # To change color:
                        self.change_color()
                        # To change theme:
                        self.change_theme()
                        plt.style.use(self.selected_theme)

                        self.frame_counter_img_3 = i + c
                        range_min_3 = 2 * int(((self.frame_counter_img_3 - 100) + abs(self.frame_counter_img_3 - 100)) / 2)
                        x_axis_3 = self.first_col_3[range_min_3:2 * self.frame_counter_img_3]
                        y_axis_3 = self.second_col_3[range_min_3:2 * self.frame_counter_img_3]
                        ax_3 = self.figureemg_3.gca()

                        ax_3.set_visible(self.status_3)

                        ax_3.cla()
                        ax_3.axes.get_xaxis().set_visible(False)
                        ax_3.spines[["right", "bottom", "top"]].set_visible(False)
                        ax_3.set_ylim(min(self.second_col_3) - 0.5, max(self.second_col_3) + 0.5)
                        ax_3.set_facecolor((1, 1, 1))
                        ax_3.grid(True)
                        ax_3.plot(x_axis_3, y_axis_3, color=self.selected_color)
                        self.canvasemg_3.draw()
                    self.canvasemg_3.flush_events()
                    return lines
                self.ani_img_3 = FuncAnimation(self.figureemg_3, update,
                                               frames=100,
                                               interval=self.speed, blit=True)
            else:
                self.flag_img_3 = False
        except Exception as e:
            print(e)

    def zoom_in(self):
        channel = self.comboBox.currentIndex()
        first_col = self.first_col_1
        second_col = self.second_col_1
        canv = self.canvasemg_1
        frame_counter = self.frame_counter_img_1
        figure = self.figureemg_1
        if channel == 0:
            first_col = self.first_col_1
            second_col = self.second_col_1
            canv = self.canvasemg_1
            frame_counter = self.frame_counter_img_1
            figure = self.figureemg_1
        elif channel == 1:
            first_col = self.first_col_2
            second_col = self.second_col_2
            canv = self.canvasemg_2
            frame_counter = self.frame_counter_img_2
            figure = self.figureemg_2
        elif channel == 2:
            first_col = self.first_col_3
            second_col = self.second_col_3
            canv = self.canvasemg_3
            frame_counter = self.frame_counter_img_3
            figure = self.figureemg_3
        try:
            # To change color:
            self.change_color()
            # To change theme:
            self.change_theme()
            plt.style.use(self.selected_theme)

            range_min_1 = 2 * int(((frame_counter - 100) + abs(frame_counter - 100)) / 2)
            x_axis_1 = first_col[range_min_1:2 * frame_counter]
            y_axis_1 = second_col[range_min_1:2 * frame_counter]
            figure.clear()
            ax_1 = figure.add_subplot(111)
            ax_1.set_facecolor((1, 1, 1))
            ax_1.grid(True)
            ax_1.axes.get_xaxis().set_visible(False)
            ax_1.spines[["right", "bottom", "top"]].set_visible(False)
            ax_1.margins(x=-0.3, y=0.05)
            ax_1.plot(x_axis_1, y_axis_1, color=self.selected_color)
            canv.draw()
            canv.flush_events()
        except Exception as e:
            print(e)

    def zoom_out(self):
        channel = self.comboBox.currentIndex()
        first_col = self.first_col_1
        second_col = self.second_col_1
        canv = self.canvasemg_1
        frame_counter = self.frame_counter_img_1
        figure = self.figureemg_1
        if channel == 0:
            first_col = self.first_col_1
            second_col = self.second_col_1
            canv = self.canvasemg_1
            frame_counter = self.frame_counter_img_1
            figure = self.figureemg_1
        elif channel == 1:
            first_col = self.first_col_2
            second_col = self.second_col_2
            canv = self.canvasemg_2
            frame_counter = self.frame_counter_img_2
            figure = self.figureemg_2
        elif channel == 2:
            first_col = self.first_col_3
            second_col = self.second_col_3
            canv = self.canvasemg_3
            frame_counter = self.frame_counter_img_3
            figure = self.figureemg_3
        try:
            # To change color:
            self.change_color()
            # To change theme:
            self.change_theme()
            plt.style.use(self.selected_theme)

            range_min_1 = 2 * int(((frame_counter - 100) + abs(frame_counter - 100)) / 2)
            x_axis_1 = first_col[range_min_1:2 * frame_counter]
            y_axis_1 = second_col[range_min_1:2 * frame_counter]
            figure.clear()
            ax_1 = figure.add_subplot(111)
            ax_1.set_facecolor((1, 1, 1))
            ax_1.grid(True)
            ax_1.set_facecolor((1, 1, 1))
            ax_1.grid(True)
            ax_1.axes.get_xaxis().set_visible(False)
            ax_1.spines[["right", "bottom", "top"]].set_visible(False)
            ax_1.margins(x=0.05, y=2)
            ax_1.plot(x_axis_1, y_axis_1, color=self.selected_color)
            canv.draw()
            canv.flush_events()
        except Exception as e:
            print(e)

    def increase_speed(self):
        channel = self.comboBox.currentIndex()
        if channel == 0:
            second_col = self.second_col_1
        elif channel == 1:
            second_col = self.second_col_2
        elif channel == 2:
            second_col = self.second_col_3
        if self.speed < 5:
            self.speed = 5
            print("reached the limits")
        else:
            self.speed -= 20
        print(self.speed)

    def decrease_speed(self):
        if self.speed > 300:
            self.speed = 300
            print("reached the limits")
        else:
            self.speed += 25
        print(self.speed)

    def add_label(self):
        txt = self.lineEdit.text()
        current_item = self.comboBox.currentText()
        index = self.combo_items.index(current_item)
        self.combo_items[index] = txt
        self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox.addItems(self.combo_items)
        self.comboBox_2.addItems(self.combo_items)
        self.lineEdit.clear()

    def change_color(self):
        self.selected_color = self.comboBox_3.currentText()

    def change_theme(self):
        self.selected_theme = self.comboBox_4.currentText()

    def hide_signal(self):
        channel = self.comboBox.currentIndex()
        if channel == 0:
            self.status_1 = False
        elif channel == 1:
            self.status_2 = False
        elif channel == 2:
            self.status_3 = False

    def show_signal(self):
        channel = self.comboBox.currentIndex()
        if channel == 0:
            self.status_1 = True
        elif channel == 1:
            self.status_2 = True
        elif channel == 2:
            self.status_3 = True

    def spectrogram(self):
        channel = self.comboBox_2.currentIndex()
        second_col = self.second_col_1
        if channel == 0:
            second_col = self.second_col_1
        elif channel == 1:
            second_col = self.second_col_2
        elif channel == 2:
            second_col = self.second_col_3
        try:
            self.min = self.horizontalSlider.value()
            self.max = self.horizontalSlider_2.value()
            ax = self.figure_2.gca()
            ax.cla()
            ax.set_xlim(second_col[self.min], second_col[self.max])
            # ax.set_xlim(self.min, self.max)
            data = second_col[self.min: self.max]
            ax.specgram(data, Fs=32000, cmap=self.pallete)
            print(self.pallete)
            self.figure_canvas_2.draw()
            self.figure_canvas_2.flush_events()
        except Exception as e:
            print(e)

    def change_pallete(self):
        self.pallete = self.comboBox_5.currentText()
        print(self.pallete)




    def save_figure(self, folder, combo_box):
        channel = 0
        figure = self.figureemg_1
        if combo_box == 1:
            channel = self.comboBox.currentIndex()
            if channel == 0:
                figure = self.figureemg_1
            elif channel == 1:
                figure = self.figureemg_2
            elif channel == 2:
                figure = self.figureemg_3
        elif combo_box == 2:
            channel = self.comboBox_2.currentIndex()
        if folder == "Signals":
            figure.savefig(f"./Screenshots/{folder}/{self.comboBox.itemText(channel)}.pdf", bbox_inches='tight')
            print("Figure printed")
        elif folder == "Spectrogram":
            self.figure_2.savefig(f"./Screenshots/{folder}/{self.comboBox_2.itemText(channel)} spectrogram.pdf", bbox_inches='tight')
            print("Figure printed")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.setText(_translate("MainWindow", "Start"))
        self.pushButton_4.setText(_translate("MainWindow", "Zoom-In"))
        self.pushButton_5.setText(_translate("MainWindow", "Zoom-Out"))
        self.pushButton_3.setText(_translate("MainWindow", "Add Signal Name"))
        self.pushButton_6.setText(_translate("MainWindow", "Print"))
        self.pushButton_19.setText(_translate("MainWindow", "Speed +"))
        self.pushButton_20.setText(_translate("MainWindow", "Speed -"))
        self.pushButton_7.setText(_translate("MainWindow", "Show"))
        self.pushButton_8.setText(_translate("MainWindow", "Print"))
        self.label.setText(_translate("MainWindow", "Spectrogram"))
        self.label_2.setText(_translate("MainWindow", "Change Signal"))
        self.label_3.setText(_translate("MainWindow", "Change Color"))
        self.label_4.setText(_translate("MainWindow", "Change Theme"))
        self.pushButton_9.setText(_translate("MainWindow", "Show"))
        self.pushButton_10.setText(_translate("MainWindow", "Hide"))
        self.label_5.setText(_translate("MainWindow", "Choose Channel"))
        self.label_6.setText(_translate("MainWindow", "Choose Pallete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# def plot_1(self):
    #     range_min_1 = 2 * int(((self.frame_counter_img_1 - 100) + abs(self.frame_counter_img_1 - 100)) / 2)
    #     x_axis_1 = self.first_col_1[range_min_1:2 * self.frame_counter_img_1]
    #     y_axis_1 = self.second_col_1[range_min_1:2 * self.frame_counter_img_1]
    #     ax_1 = self.figureemg_1.gca()
    #     ax_1.cla()
    #     # ax_1.set_axis_off()
    #     ax_1.axes.get_xaxis().set_visible(False)
    #     ax_1.spines[["right", "bottom", "top"]].set_visible(False)
    #     ax_1.set_ylim(min(self.second_col_1) - 0.5, max(self.second_col_1) + 0.5)
    #     # ax_1.set_title("First Signal")
    #     ax_1.set_facecolor((1, 1, 1))
    #     ax_1.grid(True)
    #     ax_1.plot(x_axis_1, y_axis_1)
    #     self.canvasemg_1.draw()
    #
    # def plot_2(self):
    #     range_min_2 = 2 * int(((self.frame_counter_img_2 - 100) + abs(self.frame_counter_img_2 - 100)) / 2)
    #     x_axis_2 = self.first_col_2[range_min_2:2 * self.frame_counter_img_2]
    #     y_axis_2 = self.second_col_2[range_min_2:2 * self.frame_counter_img_2]
    #     ax_2 = self.figureemg_2.gca()
    #     ax_2.cla()
    #     # ax_1.set_axis_off()
    #     ax_2.axes.get_xaxis().set_visible(False)
    #     ax_2.spines[["right", "bottom", "top"]].set_visible(False)
    #     ax_2.set_ylim(min(self.second_col_2) - 0.5, max(self.second_col_2) + 0.5)
    #     # ax_1.set_title("First Signal")
    #     ax_2.set_facecolor((1, 1, 1))
    #     ax_2.grid(True)
    #     ax_2.plot(x_axis_2, y_axis_2)
    #     self.canvasemg_2.draw()
    #
    # def plot_3(self):
    #     range_min_3 = 2 * int(((self.frame_counter_img_3 - 100) + abs(self.frame_counter_img_3 - 100)) / 2)
    #     x_axis_3 = self.first_col_3[range_min_3:2 * self.frame_counter_img_3]
    #     y_axis_3 = self.second_col_3[range_min_3:2 * self.frame_counter_img_3]
    #     ax_3 = self.figureemg_3.gca()
    #     ax_3.cla()
    #     # ax_1.set_axis_off()
    #     ax_3.axes.get_xaxis().set_visible(False)
    #     ax_3.spines[["right", "bottom", "top"]].set_visible(False)
    #     ax_3.set_ylim(min(self.second_col_3) - 0.5, max(self.second_col_3) + 0.5)
    #     # ax_1.set_title("First Signal")
    #     ax_3.set_facecolor((1, 1, 1))
    #     ax_3.grid(True)
    #     ax_3.plot(x_axis_3, y_axis_3)
    #     self.canvasemg_3.draw()
################################################################################
    # def playback(self):
    #     flag_img = self.flag_img_1
    #     frame_counter = self.frame_counter_img_1
    #     figure = self.figureemg_1
    #     first_col = self.first_col_1
    #     second_col = self.second_col_1
    #     canv = self.canvasemg_1
    #     channel = self.comboBox.currentIndex()
    #     print(channel)
    #     if channel == 0:
    #         flag_img = self.flag_img_1
    #         frame_counter = self.frame_counter_img_1
    #         figure = self.figureemg_1
    #         first_col = self.first_col_1
    #         canv = self.canvasemg_1
    #     elif channel == 1:
    #         flag_img = self.flag_img_2
    #         frame_counter = self.frame_counter_img_2
    #         figure = self.figureemg_2
    #         first_col = self.first_col_2
    #         canv = self.canvasemg_2
    #     elif channel == 2:
    #         flag_img = self.flag_img_3
    #         frame_counter = self.frame_counter_img_3
    #         figure = self.figureemg_3
    #         first_col = self.first_col_3
    #         canv = self.canvasemg_3
    #     try:
    #         if not flag_img:
    #             flag_img = True
    #             c = frame_counter
    #             figure.clear()
    #             lines = [ax.plot([], [])[0] for ax in figure.axes]
    #             def update(i):
    #                 if not flag_img:
    #                     self.ani_emg_1.event_source.stop()
    #                     self.canvasemg_1.flush_events()
    #                 else:
    #                     frame_counter = i + c
    #                     range_min_1 = 2 * int(
    #                         ((frame_counter - 100) + abs(frame_counter - 100)) / 2)
    #                     x_axis_1 = first_col[range_min_1:2 * frame_counter]
    #                     y_axis_1 = sec[range_min_1:2 * frame_counter]
    #                     ax_1 = self.figureemg_1.gca()
    #                     ax_1.cla()
    #                     ax_1.set_ylim(min(self.secondCol_1) - 0.5, max(self.secondCol_1) + 0.5)
    #                     ax_1.set_facecolor((1, 1, 1))
    #                     ax_1.grid(True)
    #                     ax_1.plot(x_axis_1, y_axis_1)
    #                     self.canvasemg_1.draw()
    #                 self.canvasemg_1.flush_events()
    #                 return lines
    #
    #             self.ani_emg_1 = FuncAnimation(self.figureemg_1, update,
    #                                            frames=np.arange(0, int(len(self.firstCol_1) / 2) - 100),
    #                                            interval=10, blit=True)
    #         else:
    #             self.flag_img_1 = False
    #     except Exception as e:
    #         print(e)
