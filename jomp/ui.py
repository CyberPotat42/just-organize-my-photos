from PyQt6 import QtCore, QtGui, QtWidgets


class AppUI:
    def setupUi(self, App):
        App.setObjectName("App")
        App.resize(940, 770)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(App.sizePolicy().hasHeightForWidth())
        App.setSizePolicy(sizePolicy)
        App.setMinimumSize(QtCore.QSize(940, 770))
        App.setMaximumSize(QtCore.QSize(940, 770))
        self.canvas = QtWidgets.QGraphicsView(App)
        self.canvas.setGeometry(QtCore.QRect(10, 10, 611, 611))
        self.canvas.setMouseTracking(True)

        self.canvas.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.canvas.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.canvas.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents
        )

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

        # Create buttons using a helper function
        self.btn_prev = self.createButton("btn_prev", 10, self.verticalLayoutWidget)
        self.btn_del = self.createButton("btn_del", 10, self.verticalLayoutWidget)
        self.btn_next = self.createButton("btn_next", 10, self.verticalLayoutWidget)

        # Add buttons to actionsHolder layout
        self.actionsHolder.addWidget(self.btn_prev)
        self.actionsHolder.addWidget(self.btn_del)
        self.actionsHolder.addWidget(self.btn_next)

        # Add actionsHolder layout to pathHolder layout
        self.pathHolder.addLayout(self.actionsHolder)

        self.path_btn = self.createButton("path_btn", 10, self.verticalLayoutWidget)
        self.pathHolder.addWidget(self.path_btn)

        self.gridLayoutWidget = QtWidgets.QWidget(App)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 620, 941, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.foldersGrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.foldersGrid.setContentsMargins(10, 11, 10, 11)
        self.foldersGrid.setSpacing(10)

        self.createSortingButtons(App)

        self.info_text = QtWidgets.QLabel(App)
        self.info_text.setGeometry(QtCore.QRect(630, 10, 301, 201))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info_text.setFont(font)
        self.info_text.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
            | QtCore.Qt.AlignmentFlag.AlignTop
        )

        self.info_text.setWordWrap(True)
        self.info_text.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextSelectableByMouse
        )

        self.info_text.setObjectName("info_text")
        self.path_text = QtWidgets.QLabel(App)
        self.path_text.setGeometry(QtCore.QRect(630, 270, 301, 201))

        font = QtGui.QFont()
        font.setPointSize(10)
        self.path_text.setFont(font)
        self.path_text.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom
            | QtCore.Qt.AlignmentFlag.AlignLeading
            | QtCore.Qt.AlignmentFlag.AlignLeft
        )

        self.path_text.setWordWrap(True)
        self.path_text.setObjectName("path_text")
        self.path_text.setTextInteractionFlags(
            QtCore.Qt.TextInteractionFlag.TextSelectableByMouse
        )

        self.retranslateUi(App)
        QtCore.QMetaObject.connectSlotsByName(App)

    def createButton(self, name, font_size, parent):
        button = QtWidgets.QPushButton(parent)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
            QtWidgets.QSizePolicy.Policy.MinimumExpanding,
        )

        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(font_size)
        button.setFont(font)
        button.setObjectName(name)

        return button

    def createSortingButtons(self, App):
        buttons_info = [
            {"name": "bt1", "pos": (0, 0)},
            {"name": "bt2", "pos": (0, 1)},
            {"name": "bt3", "pos": (0, 2)},
            {"name": "bt4", "pos": (0, 3)},
            {"name": "bt5", "pos": (0, 4)},
            {"name": "bt6", "pos": (0, 5)},
            {"name": "bt7", "pos": (1, 0)},
            {"name": "bt8", "pos": (1, 1)},
            {"name": "bt9", "pos": (1, 2)},
            {"name": "bt0", "pos": (1, 3)},
            {"name": "btS", "pos": (1, 4)},
            {"name": "btE", "pos": (1, 5)},
        ]

        # Create buttons and store references as attributes of the class
        for button_info in buttons_info:
            button = self.createButton(button_info["name"], 10, self.gridLayoutWidget)

            # Store the button reference as an attribute
            setattr(self, button_info["name"], button)

            # Add the button to the grid layout
            self.foldersGrid.addWidget(
                button, button_info["pos"][0], button_info["pos"][1], 1, 1
            )

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
