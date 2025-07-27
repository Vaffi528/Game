from modules.package import *
from .screen import Screen

class SettingsScreen(Screen):
    def __init__(self, widgets, width, height):
        super().__init__(widgets, width, height)
    
    def setsize(self, width, height) -> None:
        pass

    def setposition(self) -> None:
        self.layout_ = QVBoxLayout()
        self.layouth = QHBoxLayout()
        self.layout_.addWidget(self.widgets.nslider)
        self.layouth.addWidget(self.widgets.ok)
        self.layouth.addWidget(self.widgets.cancel)
        self.layout_.addLayout(self.layouth)
        self.setLayout(self.layout_)