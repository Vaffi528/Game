from modules.package import *
from .screen import Screen

class EndScreen(Screen):
    def __init__(self, widgets, width, height):
        super().__init__(widgets, width, height)
    
    def setsize(self, width, height) -> None:
        w, h = int(width*0.4), int(height*0.15)
        self.widgets.quit.setMaximumSize(w, h)

    def setposition(self) -> None:
        #set all elements on the screen
        self.layout_ = QVBoxLayout()
        grid = QGridLayout()
        grid.setSpacing(int(self.widgets.continue_.size().height()/0.15*0.125))
        grid.addWidget(self.widgets.winner, 0,0)
        grid.addWidget(self.widgets.quit, 1,0)
        self.layout_.addLayout(grid)
        self.setLayout(self.layout_)
        
    def subscribe(self, main):
        self.widgets.quit.clicked.connect(lambda: main.updateScreen('Start'))

        self.widgets.quit_short.triggered.connect(lambda: main.updateScreen('Start'))
        self.addAction(self.widgets.quit_short)
        