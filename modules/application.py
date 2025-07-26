from .package import *
from .greetscreen import GreetScreen
from .widgets import SharedWidgets
class Main(QWidget):
    def __init__(self):
        super().__init__()
        #set data
        self.data = self.load()
        self.widgets = SharedWidgets()
        self.screens = {'Start': GreetScreen(self.widgets),
                                            }
        self.current_screen = 'Start'
        self.n = 5; self.k = 1; self.a = 2; self.b = 2
        
        #set window parametrs
        self.showFullScreen()
        self.setWindowTitle('Game')

    def updateScreen(self, text):
        self.current_screen = text
        self.setLayout(self.screens[self.current_screen].layout)
        

    def load(self):
        with open('data/data.json', "r", encoding='utf-8') as file:
            return json.load(file)
    
    def dumps(self):
        with open('data/data.json', "w", encoding='utf-8') as file:
            json.dump(self.data, file)

    def run(self, app):
        self.widgets.subscribe(self.updateScreen)
        self.setLayout(self.screens[self.current_screen].layout)
        self.show()
        app.exec_()

    def closeEvent(self, event):
        try: self.terminate()
        except: None
        finally: event.accept()