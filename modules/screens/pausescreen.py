from modules.package import *
from .screen import Screen

class PauseScreen(Screen):
    def __init__(self, widgets, width, height):
        super().__init__(widgets, width, height)
    
    def setsize(self, width, height) -> None:
        w, h = int(width*0.4), int(height*0.15)
        self.widgets.endgame.setMaximumSize(w, h)
        self.widgets.continue_.setMaximumSize(w, h)

    def setposition(self) -> None:
        #set all elements on the screen
        self.layout_ = QVBoxLayout()
        grid = QGridLayout()
        grid.setSpacing(int(self.widgets.continue_.size().height()/0.15*0.125))
        grid.addWidget(self.widgets.continue_, 0,0)
        grid.addWidget(self.widgets.endgame, 1,0)
        self.layout_.addLayout(grid)
        self.setLayout(self.layout_)

    def endgame(self, main):
        self.widgets.update_sticks(main.data['n'])
        main.screens['Play'].reset_data(main)
        self.widgets.next.setDisabled(1)
        
    def subscribe(self, main):
        self.widgets.continue_.clicked.connect(lambda: main.updateScreen('Play'))
        self.widgets.endgame.clicked.connect(lambda: main.updateScreen('Start'))
        self.widgets.endgame.clicked.connect(lambda: self.endgame(main))

        self.widgets.continue_short.triggered.connect(lambda: main.updateScreen('Play'))
        self.widgets.end_short.triggered.connect(lambda: main.updateScreen('Start'))
        self.widgets.end_short.triggered.connect(lambda: self.endgame(main))

        self.addAction(self.widgets.continue_short)
        self.addAction(self.widgets.end_short)
        