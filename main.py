import sys
import random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle("Рисование круга")
        self.circles = []
        self.pushButton.clicked.connect(self.draw_random_circle)

    def draw_random_circle(self):
        # Генерация случайных размеров и положения круга
        radius = random.randint(20, 100)
        x = random.randint(0, self.width() - radius * 2)
        y = random.randint(0, self.height() - radius * 2)

        self.circles.append((x, y, radius))
        self.update()  # Перерисовываем окно

    def paintEvent(self, event):
        painter = QPainter(self)
        for x, y, radius in self.circles:
            painter.setBrush(QColor("yellow"))
            painter.setPen(Qt.GlobalColor.transparent)
            painter.drawEllipse(x, y, radius * 2, radius * 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())
