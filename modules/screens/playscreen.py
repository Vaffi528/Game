from modules.package import *
from .screen import Screen
from modules.computer_modes.rule1 import Rule1Mode

class PlayScreen(Screen):
    def __init__(self, widgets, width, height):
        super().__init__(widgets, width, height)
        self.turn = 0
        self.picked_stickes = 0
        self.total_quantity = 0
        self.gamemode = [self.rule1_logic]
        self.computer_gamemode = [[Rule1Mode.mode1]]
    
    def setsize(self, width, height) -> None:
        self.widgets.pause.setFixedSize(int(height/25.75), int(height/25.75))
        self.stickwidth, self.stickheight = int(width/64), int(height*0.3)
        for stick in self.widgets.sticks:
            stick.setFixedSize(self.stickwidth, self.stickheight)
        self.widgets.next.setFixedSize(int(width*0.2), int(height*0.09))

    def setposition(self) -> None:
        self.layout_ = QVBoxLayout()
        self.layout_.setContentsMargins(10, 10, 10, 10)

        sticks_widget = QWidget()
        self.sticks_layout = QHBoxLayout(sticks_widget)
        self.sticks_layout.setAlignment(Qt.AlignCenter)
        self.sticks_layout.setSpacing(int((self.widgets.sticks[0].size().width()*64)/320))
        
        for stick in self.widgets.sticks:
            self.sticks_layout.addWidget(stick)
        
        self.layout_.addWidget(self.widgets.pause, 0, Qt.AlignLeft | Qt.AlignTop)
        self.layout_.addWidget(self.widgets.queue, 0, Qt.AlignHCenter)
        self.layout_.addWidget(sticks_widget, 10)
        self.layout_.addWidget(self.widgets.next, 2, Qt.AlignHCenter | Qt.AlignTop)
        
        self.setLayout(self.layout_)
    
    def subscribe_computer(self, main):
        if main.data['computer']:
            self.computer_gamemode[main.data['gamemode']][main.data['difficulty']-1](self.widgets.sticks, self, main)
    
    def subscribe_computer_turn(self,main):
        if main.data['computer_turn']:
            self.subscribe_computer(main)
    
    #gamemodes logic:
    def rule1_logic(self, main):
        self.picked_stickes += 1
        self.total_quantity += 1
        if self.total_quantity == main.data['n']:
            self.reset(main)
            return
        if not self.widgets.next.isEnabled():
            self.widgets.next.setDisabled(0)
        if self.picked_stickes == main.data['k']:
            self.update_turn_data(main)
    
    def update_turn_data(self, main=None):
        self.turn = not self.turn
        self.widgets.queue.setText(f'{self.turn+1} Player turn')
        self.widgets.next.setDisabled(1)
        self.picked_stickes = 0
        if main:
            self.subscribe_computer(main)


    def update_turn(self, main):
        #check for the shortcut
        if self.widgets.next.isEnabled():
           self.update_turn_data(main)
    
    def reset(self, main):
        self.widgets.winner.setText(f'{self.turn+1} Player win!')
        self.reset_data(main)
        main.updateScreen('End')
        
    def reset_data(self, main):
        self.widgets.queue.setText('1 Player turn')
        self.turn = 0
        self.picked_stickes = 0
        self.total_quantity = 0
        self.widgets.next.setDisabled(1)
        self.widgets.update_sticks(main.data['n'])

    def subscribe(self, main) -> None:
        #computer turn check
        self.widgets.play.clicked.connect(lambda: self.subscribe_computer_turn(main))

        for i, stick in enumerate(self.widgets.sticks):
            stick.clicked.connect(lambda value, ind=i: self.widgets.sticks[ind].setDisabled(1))
            stick.clicked.connect(lambda: self.gamemode[main.data['gamemode']](main))
        

        self.widgets.next.clicked.connect(lambda: self.update_turn(main))
        self.widgets.next_short.triggered.connect(lambda: self.update_turn(main))
        self.addAction(self.widgets.next_short)

        self.widgets.pause.clicked.connect(lambda: main.updateScreen(self.widgets.pause.text()))
        self.widgets.pause_short.triggered.connect(lambda: main.updateScreen(self.widgets.pause.text()))
        self.addAction(self.widgets.pause_short)