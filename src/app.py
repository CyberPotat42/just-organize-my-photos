# импортируем только необходимые модули PyQt5
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QFileDialog
from PyQt5.QtCore import Qt, QEvent, QFile
from PyQt5.QtGui import QPixmap

# импортируем все остальное
from functools import partial
from glob import glob
from PIL import Image

from func import * # полезные функции
from ui import *  # настройки интерфейса


class app(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_App()
        self.ui.setupUi(self)
        self.show()

        self.image_list, self.folders = [], {}
        self.image_id, self.img_count = 0, 0
        self.image, self.scene = None, None
        self.path, self.image_path = "", ""

        self.setChildrenFocusPolicy(Qt.ClickFocus)

        self.ui.path_btn.clicked.connect(self.selectFolder)
        self.ui.btn_next.clicked.connect(partial(self.changeImage,  1))
        self.ui.btn_prev.clicked.connect(partial(self.changeImage, -1))
        self.ui.btn_del.clicked.connect(self.deleteImage)
        self.ui.canvas.setMouseTracking(True)
        self.ui.canvas.viewport().installEventFilter(self)

        # настраиваем драгндроп
        self.ui.canvas.dropEvent = lambda e: self.open_dnd(e)
        self.ui.canvas.dragEnterEvent = lambda e: e.accept() if isAccepted(e) else e.ignore()

        self.buttons = [self.ui.bt1, self.ui.bt2, self.ui.bt3, self.ui.bt4,
                        self.ui.bt5, self.ui.bt6, self.ui.bt7, self.ui.bt8,
                        self.ui.bt9, self.ui.bt0, self.ui.btS, self.ui.btE]

        self.tags = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "Space", "Enter"]
        self.keys = [Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6,
                     Qt.Key_7, Qt.Key_8, Qt.Key_9, Qt.Key_0, Qt.Key_Space, Qt.Key_Return]

        for btn, tag in zip(self.buttons, self.tags):
            btn.setContextMenuPolicy(Qt.CustomContextMenu)
            btn.clicked.connect(partial(self.move2folder, folder=tag))
            btn.customContextMenuRequested.connect(partial(self.move2folder, folder=tag, change=True))

    def setChildrenFocusPolicy(self, policy):
        def recursiveSetChildFocusPolicy (parentQWidget):
            for childQWidget in parentQWidget.findChildren(QtWidgets.QWidget):
                childQWidget.setFocusPolicy(policy)
                recursiveSetChildFocusPolicy(childQWidget)
        recursiveSetChildFocusPolicy(self)

    def selectFolder(self):
        self.checkPath(self.pickDirectory())

    def pickDirectory(self, text="Select Directory"):
        return str(QFileDialog.getExistingDirectory(self, text))

    def open_dnd(self, event):
        path = isAccepted(event)
        if path: self.checkPath(path)

    def checkPath(self, folder):
        if folder == "": return None
        self.path = folder
        self.image_list = [
            item.replace("\\", "/") for i in [
                glob(f"{self.path}/*{ext}") for ext in \
                ["jpg","jpeg","png","jfif","bmp","gif","pbm","pgm","ppm","xbm","xpm"]
            ] for item in i
        ]
        self.img_count, self.image_id = len(self.image_list), 0
        self.ui.path_text.setText(f"path: {self.path} ({self.img_count} photo)")
        if self.img_count == 0: return None
        self.displayImg()

    def deleteImage(self):
        if self.img_count > 0:
            del_img = self.image_list.pop(self.image_id)
            self.img_count = len(self.image_list)
            if self.image_id == self.img_count: self.image_id -= 1
            if self.img_count > 0: self.displayImg()
            else: self.clearPreview()
            self.image.close()
            if QtWidgets.QApplication.keyboardModifiers() == Qt.ControlModifier:
                os.remove(del_img)
            else:
                QFile.moveToTrash(del_img)

    def clearPreview(self):
        self.scene.clear()
        self.ui.canvas.viewport().update()
        self.ui.path_text.setText(f"File: Null\nPath: {self.path}")
        self.ui.info_text.setText(
            f"Image {self.image_id + 1} / {self.img_count}\n[ all files sorted ]")

    def displayImg(self):
        if self.img_count <= 0: return None
        self.image_path = self.image_list[self.image_id]
        if os.path.isfile(self.image_path):
            w, h = self.ui.canvas.width(), self.ui.canvas.height()
            self.scene = QtWidgets.QGraphicsScene(self)
            # Load the pixmap from the image path
            pixmap = QPixmap(self.image_path)
            # Scale with smooth transformation for better quality
            scaled_pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            # Create the QGraphicsPixmapItem with the scaled pixmap
            item = QtWidgets.QGraphicsPixmapItem(scaled_pixmap)
            self.scene.addItem(item)
            self.ui.canvas.setScene(self.scene)
            self.ui.path_text.setText(f"File: {os.path.basename(self.image_path)}\nPath: {self.path}")
            try:
                self.image = Image.open(self.image_path)
                self.ui.info_text.setText(
                    f"Image {self.image_id + 1} / {self.img_count}\n" +
                    f"Res: {' × '.join([str(i) for i in self.image.size])}\n" +
                    f"Size: {convert_size(os.path.getsize(self.image_path))}\n" +
                    f"Date: {getModifyDate(self.image_path)}" + # full: %d.%m.%Y %H:%M:%S
                    f"\n\nQuality: {format_res(self.image.size, print_name=True)}")
            except OSError:
                self.ui.info_text.setText(
                    f"Image {self.image_id + 1} / {self.img_count}\nRes: Null\n" +
                    f"Size: {convert_size(os.path.getsize(self.image_path))}\nDate: Null\n" +
                    "[ corrupted image file ]")
            self.ui.info_text.setCursor(Qt.IBeamCursor)

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                viewFile(self.image_path)
            elif event.button() == Qt.RightButton:
                showInExplorer(self.image_path)
        return super().eventFilter(source, event)

    def changeImage(self, order):
        self.image_id += order
        if self.image_id == self.img_count:
            self.image_id = 0
        elif self.image_id < 0:
            self.image_id = self.img_count-1
        self.displayImg()

    def move2folder(self, folder, change=False):
        modifier = QtWidgets.QApplication.keyboardModifiers()
        if change or folder not in self.folders.keys() \
        or modifier in (Qt.ControlModifier, Qt.ShiftModifier):
            path = self.pickDirectory("Select target directory")
            if path == "" : return None
            self.folders |= {folder: path}
            self.buttons[self.tags.index(folder)].setText("Key " + folder + ":\n" + os.path.basename(path))

        if self.img_count <= 0: return None # перемещать нечего
        if folder in self.folders.keys():
            self.image.close() # нужно закрывать файл перед перемещением
            img_pth = self.image_list.pop(self.image_id)
            new_pth = os.path.join(self.folders[folder], os.path.basename(img_pth))
            #* делать проверку, существует ли файл
            if os.path.isfile(new_pth):
                print("файл уже существует", smartRename(new_pth))
                new_pth = smartRename(new_pth)

            os.replace(img_pth, new_pth)
            self.img_count = len(self.image_list)
            if self.image_id == self.img_count: self.image_id -= 1
            if self.img_count > 0: self.displayImg()
            else: self.clearPreview()

    def keyPressEvent(self, event):
        k = event.key()
        if k == Qt.Key_Delete:  self.deleteImage()
        elif k == Qt.Key_Right: self.changeImage(1)
        elif k == Qt.Key_D:     self.changeImage(1)
        elif k == Qt.Key_Left:  self.changeImage(-1)
        elif k == Qt.Key_A:     self.changeImage(-1)
        elif k in self.keys: self.move2folder(self.tags[self.keys.index(k)])
        else: QWidget.keyPressEvent(self, event)


if __name__ == "__main__": #? for test
    from PyQt5.QtWidgets import QApplication
    from sys import exit as sys_exit
    app, ui = QApplication([]), app()
    sys_exit(app.exec_())
