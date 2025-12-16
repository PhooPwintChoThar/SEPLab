import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.frame_no = 0
        self.images = []
        for i in range(1, 21):
            pixmap = QPixmap("images/frame_" + str(i + 1) + ".png")
            self.images.append(pixmap)

        timer = QTimer(self)
        timer.timeout.connect(self.update_value)
        timer.start(75)

        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("sounds/rabbit_jump.wav"))

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawPixmap(QRect(0, 0, 320, 320), self.images[self.frame_no])
        p.end()

    def update_value(self):
        self.frame_no += 1
        if self.frame_no >= 20:
            self.frame_no = 0
            self.QSE.play()
        self.update()


class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.anim_area = Animation_area()
        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        layout.addWidget(QPushButton("Pause"))
        self.setLayout(layout)
        self.setMinimumSize(330, 400)


def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())