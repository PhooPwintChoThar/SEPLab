import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.setFixedSize(300, 300)
    
    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)
        
        # Draw carrot
        p.setBrush(QColor(255, 127, 0))  # Orange color
        p.drawPolygon([
            QPoint(100, 100),
            QPoint(130, 80),
            QPoint(127, 127)
        ])
        
        # Draw carrot leaves
        p.setBrush(QColor(0, 127, 0))  # Green color
        p.drawPolygon([
            QPoint(130, 80),
            QPoint(150, 60),
            QPoint(127, 127)
        ])
        
        # Draw rabbit body (circle)
        p.setBrush(QColor(200, 200, 200))  # Light gray
        p.drawEllipse(100, 150, 100, 100)
        
        # Draw rabbit ear
        p.setBrush(QColor(255, 180, 180))  # Pink for inner ear
        p.drawEllipse(160, 150, 20, 40)
        
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
