from .package import *

class SharedWidgets():
    def __init__(self):
        #create buttons
        self.play = QPushButton("Play")
        self.settings = QPushButton("Settings")
        self.info = QPushButton("Info")
        self.exit = QPushButton("Exit")

        #set style
        self.play.setFont(QtGui.QFont("monospace", 12))
        self.settings.setFont(QtGui.QFont("monospace", 12))
        self.info.setFont(QtGui.QFont("monospace", 12))
        self.exit.setFont(QtGui.QFont("monospace", 12))

        #set size of all elements
        self.play.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.settings.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.info.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.exit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    def subscribe(self, update_screen):
        self.play.clicked.connect(lambda: update_screen(self.play.text()))
        self.exit.clicked.connect(sys.exit)