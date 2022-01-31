# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Projects\PhotoOrganizer\new_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_App(object):
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(940, 770)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(App.sizePolicy().hasHeightForWidth())
        App.setSizePolicy(sizePolicy)
        App.setMinimumSize(QtCore.QSize(940, 770))
        App.setMaximumSize(QtCore.QSize(940, 770))
        self.canvas = QtWidgets.QGraphicsView(App)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 611, 611))
        self.canvas.setMouseTracking(True)
        self.canvas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.canvas.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.canvas.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.canvas.setInteractive(True)
        self.canvas.setObjectName("canvas")
        self.verticalLayoutWidget = QtWidgets.QWidget(App)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(620, 480, 322, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.pathHolder = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.pathHolder.setContentsMargins(11, 10, 10, 0)
        self.pathHolder.setSpacing(10)
        self.pathHolder.setObjectName("pathHolder")
        self.actionsHolder = QtWidgets.QHBoxLayout()
        self.actionsHolder.setSpacing(10)
        self.actionsHolder.setObjectName("actionsHolder")
        self.btn_prev = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_prev.sizePolicy().hasHeightForWidth())
        self.btn_prev.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_prev.setFont(font)
        self.btn_prev.setObjectName("btn_prev")
        self.actionsHolder.addWidget(self.btn_prev)
        self.btn_del = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_del.sizePolicy().hasHeightForWidth())
        self.btn_del.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")
        self.actionsHolder.addWidget(self.btn_del)
        self.btn_next = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_next.setFont(font)
        self.btn_next.setObjectName("btn_next")
        self.actionsHolder.addWidget(self.btn_next)
        self.pathHolder.addLayout(self.actionsHolder)
        self.path_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_btn.sizePolicy().hasHeightForWidth())
        self.path_btn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_btn.setFont(font)
        self.path_btn.setObjectName("path_btn")
        self.pathHolder.addWidget(self.path_btn)
        self.gridLayoutWidget = QtWidgets.QWidget(App)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 620, 941, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.foldersGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.foldersGrid.setContentsMargins(10, 11, 10, 11)
        self.foldersGrid.setSpacing(10)
        self.foldersGrid.setObjectName("foldersGrid")
        self.bt6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt6.sizePolicy().hasHeightForWidth())
        self.bt6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt6.setFont(font)
        self.bt6.setObjectName("bt6")
        self.foldersGrid.addWidget(self.bt6, 0, 5, 1, 1)
        self.bt2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt2.sizePolicy().hasHeightForWidth())
        self.bt2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt2.setFont(font)
        self.bt2.setObjectName("bt2")
        self.foldersGrid.addWidget(self.bt2, 0, 1, 1, 1)
        self.bt4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt4.sizePolicy().hasHeightForWidth())
        self.bt4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt4.setFont(font)
        self.bt4.setObjectName("bt4")
        self.foldersGrid.addWidget(self.bt4, 0, 3, 1, 1)
        self.bt3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt3.sizePolicy().hasHeightForWidth())
        self.bt3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt3.setFont(font)
        self.bt3.setObjectName("bt3")
        self.foldersGrid.addWidget(self.bt3, 0, 2, 1, 1)
        self.bt5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt5.sizePolicy().hasHeightForWidth())
        self.bt5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt5.setFont(font)
        self.bt5.setObjectName("bt5")
        self.foldersGrid.addWidget(self.bt5, 0, 4, 1, 1)
        self.bt1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt1.sizePolicy().hasHeightForWidth())
        self.bt1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt1.setFont(font)
        self.bt1.setObjectName("bt1")
        self.foldersGrid.addWidget(self.bt1, 0, 0, 1, 1)
        self.bt7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt7.sizePolicy().hasHeightForWidth())
        self.bt7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt7.setFont(font)
        self.bt7.setObjectName("bt7")
        self.foldersGrid.addWidget(self.bt7, 1, 0, 1, 1)
        self.bt8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt8.sizePolicy().hasHeightForWidth())
        self.bt8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt8.setFont(font)
        self.bt8.setObjectName("bt8")
        self.foldersGrid.addWidget(self.bt8, 1, 1, 1, 1)
        self.bt9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt9.sizePolicy().hasHeightForWidth())
        self.bt9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt9.setFont(font)
        self.bt9.setObjectName("bt9")
        self.foldersGrid.addWidget(self.bt9, 1, 2, 1, 1)
        self.bt0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt0.sizePolicy().hasHeightForWidth())
        self.bt0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt0.setFont(font)
        self.bt0.setObjectName("bt0")
        self.foldersGrid.addWidget(self.bt0, 1, 3, 1, 1)
        self.btS = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btS.sizePolicy().hasHeightForWidth())
        self.btS.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btS.setFont(font)
        self.btS.setObjectName("btS")
        self.foldersGrid.addWidget(self.btS, 1, 4, 1, 1)
        self.btE = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btE.sizePolicy().hasHeightForWidth())
        self.btE.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btE.setFont(font)
        self.btE.setObjectName("btE")
        self.foldersGrid.addWidget(self.btE, 1, 5, 1, 1)
        self.info_text = QtWidgets.QLabel(App)
        self.info_text.setGeometry(QtCore.QRect(630, 10, 301, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_text.setFont(font)
        self.info_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info_text.setWordWrap(True)
        self.info_text.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.info_text.setObjectName("info_text")
        self.path_text = QtWidgets.QLabel(App)
        self.path_text.setGeometry(QtCore.QRect(630, 270, 301, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_text.setFont(font)
        self.path_text.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.path_text.setWordWrap(True)
        self.path_text.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.path_text.setObjectName("path_text")

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def retranslateUi(self, App):
        _translate = QtCore.QCoreApplication.translate
        App.setWindowTitle(_translate("App", "Just organize my photos"))
        self.btn_prev.setText(_translate("App", "<"))
        self.btn_del.setText(_translate("App", "Delete"))
        self.btn_next.setText(_translate("App", ">"))
        self.path_btn.setText(_translate("App", "Select Path"))
        self.bt6.setText(_translate("App", "Key 6"))
        self.bt2.setText(_translate("App", "Key 2"))
        self.bt4.setText(_translate("App", "Key 4"))
        self.bt3.setText(_translate("App", "Key 3"))
        self.bt5.setText(_translate("App", "Key 5"))
        self.bt1.setText(_translate("App", "Key 1"))
        self.bt7.setText(_translate("App", "Key 7"))
        self.bt8.setText(_translate("App", "Key 8"))
        self.bt9.setText(_translate("App", "Key 9"))
        self.bt0.setText(_translate("App", "Key 0"))
        self.btS.setText(_translate("App", "Space"))
        self.btE.setText(_translate("App", "Enter"))
        self.info_text.setText(_translate("App", "Image Info"))
        self.path_text.setText(_translate("App", "Path Info"))