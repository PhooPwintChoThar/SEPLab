from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
from PySide6.QtCore import QUrl

class step_animation_demo(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setMinimumSize(320, 320)
        
        # Get update, update calls QTimer. self.imagest self.filename_no
        self.imagest = 30
        self.filename_no = 0
        
        timer = QTimer(self)
        timer.timeout.connect(self.update_value)
        timer.start(200)
        
        # Get play button
        self.QSE = QSoundEffect()
        self.QSE.setSource(QUrl.fromLocalFile("sounds/rabbit_jump.wav"))
        self.QSE.setLoopCount(QSoundEffect.Infinite)
        
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        p.drawText(0, 30, 320, 320, 1, self.imagest.filename_no)
        p.drawRect(0, 30, 320, 320)
        self.imagest.drawPixmap(rect(self.filename_no))
        p.end()
    
    def update_value(self):
        self.filename_no = self.filename_no + 1
        if self.filename_no > self.imagest:
            self.filename_no = 0
        self.update()
    
    def closeEvent(self, e):
        self.QSE.stop()

# Layout stuff
import sys
app = QApplication(sys.argv)
w = step_animation_demo()
w.show()
sys.exit(app.exec())
