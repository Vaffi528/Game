from modules.package import *
from .screen import Screen

class SettingsScreen(Screen):
    def __init__(self, widgets, width, height):
        super().__init__(widgets, width, height)
    
    def setsize(self, width, height) -> None:
        w, h = int(width*0.25), int(height*0.04)
        self.widgets.play_computer.setMaximumSize(w,h)
        self.widgets.ok.setMaximumSize(w, h)
        self.widgets.cancel.setMaximumSize(w, h)

    def setposition(self) -> None:
        '''self.layout_ = QVBoxLayout()
        self.layouth = QHBoxLayout()
        self.gridbutts = QGridLayout()
        self.layout_.addWidget(self.widgets.nslider)
        self.layouth.addWidget(self.widgets.ok)
        self.layouth.addWidget(self.widgets.cancel)
        self.layout_.addLayout(self.layouth)
        self.setLayout(self.layout_)'''
    
        self.layout_ = QVBoxLayout()
        self.layout_.setContentsMargins(20, 20, 20, 20)
        self.layout_.setSpacing(15)
        
        #Play against computer checkbox
        self.layout_.addWidget(self.widgets.play_computer)
        
        #Difficulty level (disabled when checkbox unchecked)
        difficulty_layout = QHBoxLayout()
        difficulty_layout.addWidget(self.widgets.difficulty_lvl)
        
        difficulty_layout.addWidget(self.widgets.difficulty_combo)
        difficulty_layout.addStretch()
        self.layout_.addLayout(difficulty_layout)
        
        #Game mode radio buttons
        game_modes_layout = QGridLayout()
        game_modes_layout.setSpacing(10)
        game_modes_layout.addWidget(self.widgets.game_rules, 0,0)
        for i, button in enumerate(self.widgets.modes):
            game_modes_layout.addWidget(button, i+1,0)
        
        self.layout_.addLayout(game_modes_layout)

        #sliders
        for i, slider in enumerate(self.widgets.sliders):
            slider_layout = QHBoxLayout()
            slider_range_layout = QGridLayout()
            curr_value_layout = QVBoxLayout()
            slider_range_layout.addWidget(self.widgets.sliderlabels[i][0], 0,0)
            slider_range_layout.addWidget(slider, 0,1)
            slider_range_layout.addWidget(self.widgets.sliderlabels[i][2], 0,2)
            curr_value_layout.addWidget(self.widgets.sliderlabels[i][1], alignment=Qt.AlignHCenter)
            curr_value_layout.addLayout(slider_range_layout)
            slider_layout.addWidget(self.widgets.sliderlabels[i][3])
            slider_layout.addLayout(curr_value_layout)
            self.layout_.addLayout(slider_layout)

        
        #ok and cancel buttons
        button_layout = QHBoxLayout()
        
        button_layout.addWidget(self.widgets.ok)
        button_layout.addSpacing(int(self.widgets.play.size().height()/0.15*0.015))
        button_layout.addWidget(self.widgets.cancel)
        
        self.layout_.addLayout(button_layout)
        
        self.setLayout(self.layout_)