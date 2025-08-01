from modules.package import *
from .screen import Screen
from modules.computer_modes.rule1 import Rule1Mode
from modules.computer_modes.rule2 import Rule2Mode
from modules.computer_modes.rule3 import Rule3Mode

class PlayScreen(Screen):
    def __init__(self, widgets, width, height):
        super().__init__(widgets, width, height)
        self.turn = 0
        self.picked_stickes = 0
        self.total_quantity = 0
        self.RULES = [Rule1Mode, Rule2Mode, Rule3Mode()]
        self.gamemode = [RuleMode.rule_logic for RuleMode in self.RULES]
        self.computer_gamemode = [RuleMode.mode for RuleMode in self.RULES]
        self.update_gamemode = [RuleMode.update_turn_data for RuleMode in self.RULES]
    
    def setsize(self, width, height) -> None:
        self.widgets.pause.setFixedSize(int(height/25.75), int(height/25.75))
        self.stickwidth, self.stickheight = int(width/64), int(height*0.3)
        for stick in self.widgets.sticks:
            stick.setFixedSize(self.stickwidth, self.stickheight)
        self.widgets.next.setFixedSize(int(width*0.2), int(height*0.09))

    def setposition(self) -> None:
        self.layout_ = QVBoxLayout()
        self.layout_.setContentsMargins(10, 10, 10, 10)

        self.sticks_widget = QWidget()
        self.sticks_layout = QHBoxLayout(self.sticks_widget)
        self.sticks_layout.setAlignment(Qt.AlignCenter)
        self.sticks_layout.setSpacing(int((self.widgets.sticks[0].size().width()*64)/320))
        
        for stick in self.widgets.sticks:
            self.sticks_layout.addWidget(stick)
        
        self.layout_.addWidget(self.widgets.pause, 0, Qt.AlignLeft | Qt.AlignTop)
        self.layout_.addWidget(self.widgets.queue, 0, Qt.AlignHCenter)
        self.layout_.addWidget(self.sticks_widget, 10)
        self.layout_.addWidget(self.widgets.next, 2, Qt.AlignHCenter | Qt.AlignTop)
        
        self.setLayout(self.layout_)
    
    def subscribe_computer(self, main):
        if main.data['computer']:
            self.computer_gamemode[main.data['gamemode']](self.widgets.sticks[:main.data['n']], self, main, main.data['difficulty'])
    
    def subscribe_computer_turn(self,main):
        if main.data['computer_turn']:
            self.subscribe_computer(main)

    def update_turn(self, main):
        #check for the shortcut
        if self.widgets.next.isEnabled():
           self.update_gamemode[main.data['gamemode']](self, main)
    
    def reset(self, main):
        self.widgets.winner.setText(f'{self.turn+1} Player win!')

        pixmap = self.sticks_widget.grab()
        pixmap = pixmap.scaled(
        int(self.width()*0.6), 
        int(self.height()*0.6),
        Qt.KeepAspectRatio,
        Qt.SmoothTransformation
        )
        self.widgets.screen_.setPixmap(pixmap)

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
            stick.clicked.connect(lambda value, ind=i: self.gamemode[main.data['gamemode']](self, main, ind))
        

        self.widgets.next.clicked.connect(lambda: self.update_turn(main))
        self.widgets.next_short.triggered.connect(lambda: self.update_turn(main))
        self.addAction(self.widgets.next_short)

        self.widgets.pause.clicked.connect(lambda: main.updateScreen(self.widgets.pause.text()))
        self.widgets.pause_short.triggered.connect(lambda: main.updateScreen(self.widgets.pause.text()))
        self.addAction(self.widgets.pause_short)