from modules.package import *
from .screen import Screen

class GreetScreen(Screen):
    def __init__(self, widgets, width, height):
        super().__init__(widgets, width, height)
    
    def setsize(self, width, height) -> None:
        w, h = int(width*0.4), int(height*0.15)
        self.widgets.play.setMaximumSize(w, h)
        self.widgets.settings.setMaximumSize(w, h)
        self.widgets.info.setMaximumSize(w, h)
        self.widgets.exit.setMaximumSize(w, h)

    def setposition(self) -> None:
        #set all elements on the screen
        self.layout_ = QVBoxLayout()
        grid = QGridLayout()
        grid.setSpacing(int(self.widgets.play.size().height()/0.15*0.025))
        grid.addWidget(self.widgets.play, 0,0)
        grid.addWidget(self.widgets.settings, 1,0)
        grid.addWidget(self.widgets.info, 2,0)
        grid.addWidget(self.widgets.exit, 3,0)
        self.layout_.addLayout(grid)
        self.setLayout(self.layout_)

    def subscribe(self, **kwargs):
        self.widgets.play.clicked.connect(lambda: kwargs['update_screen'](self.widgets.play.text()))
        self.widgets.settings.clicked.connect(lambda: kwargs['update_screen'](self.widgets.settings.text()))
        self.widgets.exit.clicked.connect(sys.exit)