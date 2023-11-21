from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPaintEvent, QPainter
from PySide6.QtWidgets import QFrame

class Gui(QFrame):
    def __init__(self, agent) -> None:
        super(Gui, self).__init__()
        self.agent = agent
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setFixedSize(626, 417)

    def paintEvent(self, _: QPaintEvent) -> None:
        painter = QPainter(self)
        mar_image = QImage("fondo_mar.png")
        painter.drawImage(0, 0, mar_image)
        for fish in self.agent.fish_list:
            fish_image = QImage("pez.png")
            fish_image = fish_image.scaled(fish.size*2, fish.size)
            painter.drawImage(fish.x, fish.y, fish_image)
            #painter.fillRect(fish.x, fish.y, fish.size, fish.size//2, fish.color)
            
