from modules.package import *

class Screen(QWidget):
    def __init__(self, widgets, width, height):
        super().__init__()
        self.widgets = widgets
        self.setup(width, height)

    def setup(self, width, height) -> None:
        self.setsize(width, height)
        self.setposition()

    def setsize(self, width, height) -> None:
        pass

    def setposition(self) -> None:
        pass