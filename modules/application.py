from .package import *
from .screens.greetscreen import GreetScreen
from .screens.settingsscreen import SettingsScreen
from .widgets import SharedWidgets

class Main(QWidget):
    def __init__(self):
        super().__init__()
        #set window parametrs
        self.resize(QDesktopWidget().availableGeometry().width(), QDesktopWidget().availableGeometry().height())
        self.setWindowTitle('Game')

        #set data
        self.data = self.load()
        self.widgets = SharedWidgets(**self.data)
        self.screens = {'Start': GreetScreen(self.widgets, self.width(), self.height()),
                        'Settings': SettingsScreen(self.widgets, self.width(), self.height())}
        self.indexes = {'Start': 0, 'Settings': 1, 'Ok':0}
        self.current_screen = 'Start'
        self.stacked_layout = QStackedLayout()
        for widget in list(self.screens.values()):
            self.stacked_layout.addWidget(widget)

    def updateScreen(self, text):
        self.current_screen = text
        if text == 'Ok':
            self.data = self.load()
        self.stacked_layout.setCurrentIndex(self.indexes[self.current_screen])

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            if self.isFullScreen():
                self.showNormal()
            else:
                self.showFullScreen()
        super().keyPressEvent(event)

    def load(self):
        try:
            with open('data/data.json', "r", encoding='utf-8') as file:
                return json.load(file)
        except json.decoder.JSONDecodeError:
            data = {'n': 5, 'k': 5, 'a': 2, 'b': 2, 
                    'computer': 0, 'difficulty':1, 'gamemode':4, }
            with open('data/data.json', "w", encoding='utf-8') as file:
                json.dump(data, file)
            return data

    def run(self, app):
        self.widgets.subscribe(self.updateScreen)
        self.setLayout(self.stacked_layout)
        self.show()
        app.exec_()