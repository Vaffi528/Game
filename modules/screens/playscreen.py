from modules.package import *
from .screen import Screen

class PlayScreen(Screen):
    def __init__(self, widgets, width, height):
        super().__init__(widgets, width, height)
    
    def setsize(self, width, height) -> None:
        self.widgets.pause.setFixedSize(int(height/25.75), int(height/25.75))
        self.stickwidth, self.stickheight = int(width/64), int(height*0.3)
        for stick in self.widgets.sticks:
            stick.setFixedSize(self.stickwidth, self.stickheight)

    def setposition(self) -> None:
        self.layout_ = QVBoxLayout()
        self.layout_.setContentsMargins(10, 10, 10, 10)

        sticks_widget = QWidget()
        self.sticks_layout = QHBoxLayout(sticks_widget)
        self.sticks_layout.setAlignment(Qt.AlignCenter)
        self.sticks_layout.setSpacing(int((self.widgets.sticks[0].size().width()*64)/320))
        
        for stick in self.widgets.sticks:
            self.sticks_layout.addWidget(stick)
        
        # Компоновка элементов
        self.layout_.addWidget(self.widgets.pause, 0, Qt.AlignLeft | Qt.AlignTop)
        self.layout_.addWidget(sticks_widget, 1)
        
        self.setLayout(self.layout_)

    def subscribe(self, main) -> None:
        for i, stick in enumerate(self.widgets.sticks):
            stick.clicked.connect(lambda value, ind=i: self.widgets.sticks[ind].setDisabled(1))
        
        self.widgets.pause.clicked.connect(lambda: main.updateScreen(self.widgets.pause.text()))
        
    def update_sticks(self, main):
        while self.sticks_layout.count() > 0:
            item = self.sticks_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        for stick in self.widgets.sticks:
            stick.setFixedSize(self.stickwidth, self.stickheight)
            self.sticks_layout.addWidget(stick)
        
        self.subscribe(main)