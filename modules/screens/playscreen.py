from modules.package import *
from .screen import Screen

class PlayScreen(Screen):
    def __init__(self, widgets, width, height):
        super().__init__(widgets, width, height)
        self.turn = 0
        self.picked_stickes = 0
        self.total_quantity = 0
    
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
    
    def rule1_logic(self,main):
        self.picked_stickes += 1
        self.total_quantity += 1
        if self.total_quantity == main.data['n']:
            self.reset(main)
            return
        if not self.widgets.next.isEnabled():
            self.widgets.next.setDisabled(0)
        if self.picked_stickes == main.data['k']:
            self.update_turn()
        
    def update_turn(self):
        self.turn = not self.turn
        self.widgets.queue.setText(f'{self.turn+1} Player turn')
        self.widgets.next.setDisabled(1)
        self.picked_stickes = 0
    
    def reset(self, main):
        self.widgets.winner.setText(f'{self.turn+1} Player win!')
        self.turn = 0
        self.picked_stickes = 0
        self.total_quantity = 0
        self.widgets.next.setDisabled(1)
        self.widgets.update_sticks(main.data['n'])
        main.updateScreen('End')

    def subscribe(self, main) -> None:
        for i, stick in enumerate(self.widgets.sticks):
            stick.clicked.connect(lambda value, ind=i: self.widgets.sticks[ind].setDisabled(1))
            stick.clicked.connect(lambda: self.rule1_logic(main))
        
        self.widgets.next.clicked.connect(self.update_turn)
        self.widgets.next_short.triggered.connect(self.update_turn)
        self.addAction(self.widgets.next_short)

        self.widgets.pause.clicked.connect(lambda: main.updateScreen(self.widgets.pause.text()))
        self.widgets.pause_short.triggered.connect(lambda: main.updateScreen(self.widgets.pause.text()))
        self.addAction(self.widgets.pause_short)