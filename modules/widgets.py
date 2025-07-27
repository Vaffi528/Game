from .package import *

class SharedWidgets():
    def __init__(self, **kwargs):
        #create buttons
        ##greet
        self.play = QPushButton("Play")
        self.settings = QPushButton("Settings")
        self.info = QPushButton("Info")
        self.exit = QPushButton("Exit")
        ##settings
        self.ok = QPushButton("Ok")
        self.cancel = QPushButton("Cancel")

        #create sliders
        ##settings
        self.nslider = QSlider(Qt.Horizontal)
        self.nslider.setMinimum(5)
        self.nslider.setMaximum(50)
        self.nslider.setPageStep(1)
        self.nslider.setProperty("value", kwargs['a'])

        #set style
        self.play.setFont(QtGui.QFont("monospace", 12))
        self.settings.setFont(QtGui.QFont("monospace", 12))
        self.info.setFont(QtGui.QFont("monospace", 12))
        self.exit.setFont(QtGui.QFont("monospace", 12))

    def subscribe(self, update_screen):
        self.play.clicked.connect(lambda: update_screen(self.play.text()))
        self.settings.clicked.connect(lambda: update_screen(self.settings.text()))
        self.cancel.clicked.connect(lambda: update_screen('Start'))
        self.exit.clicked.connect(sys.exit)