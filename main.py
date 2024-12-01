import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

class Ui_MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.button = QPushButton("Round", self)

class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Рисование окружностей")
        self.setGeometry(100, 100, 600, 400)

        self.ui = Ui_MainWindow()
        self.setCentralWidget(self.ui)

        self.ui.button.clicked.connect(self.draw_random_circle)

        self.circles = []

    def draw_random_circle(self):
        radius = random.randint(20, 100)
        x = random.randint(0, self.width() - radius * 2)
        y = random.randint(0, self.height() - radius * 2)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        self.circles.append((x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, radius, color in self.circles:
            painter.setBrush(color)
            painter.setPen(Qt.GlobalColor.transparent)
            painter.drawEllipse(x, y, radius * 2, radius * 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())