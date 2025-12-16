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

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(75)

        self.running = True

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

    def toggle_animation(self):
        if self.running:
            self.timer.stop()
        else:
            self.timer.start(75)
        self.running = not self.running


class Simple_animation_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.anim_area = Animation_area()

        self.btn = QPushButton("Pause")
        self.btn.clicked.connect(self.toggle_play_pause)

        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        layout.addWidget(self.btn)
        self.setLayout(layout)

        self.setMinimumSize(330, 400)

    def toggle_play_pause(self):
        self.anim_area.toggle_animation()
        if self.anim_area.running:
            self.btn.setText("Pause")
        else:
            self.btn.setText("Play")


def main():
    app = QApplication(sys.argv)
    w = Simple_animation_window()
    w.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())