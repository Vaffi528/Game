from .package import *

class GreetScreen():
    def __init__(self, widgets):
        self.widgets = widgets
        self.setup()

    def setup(self):
        #set all elements on the screen
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.widgets.play)
        self.layout.addWidget(self.widgets.settings)
        self.layout.addWidget(self.widgets.info)
        self.layout.addStretch(1)
        self.layout.addWidget(self.widgets.exit)