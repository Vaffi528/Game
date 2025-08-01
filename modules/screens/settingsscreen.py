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
        self.layout_ = QVBoxLayout()
        self.layout_.setContentsMargins(20, 20, 20, 20)
        self.layout_.setSpacing(15)
        
        #Play against computer checkbox
        self.layout_.addWidget(self.widgets.play_computer)
        
        #Computer's turn first (disabled when 1st checkbox unchecked)
        self.layout_.addWidget(self.widgets.play_computer_turn)
        
        #Difficulty level (disabled when 1st checkbox unchecked)
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

    def change_nslider(self, value):
        for i in [1,3]:
            self.widgets.sliders[i].setMaximum(value)
            self.widgets.sliderlabels[i][2].setText(str(value))
            if self.widgets.sliders[i].value() > value:
                self.widgets.sliders[i].setValue(value)
                
        
        bslider_value = self.widgets.sliders[3].value()
        if bslider_value < int(self.widgets.sliderlabels[2][2].text()):
            self.widgets.sliders[2].setMaximum(bslider_value)
            self.widgets.sliders[3].setMinimum(bslider_value)
            self.widgets.sliderlabels[3][0].setText(str(bslider_value))
            self.widgets.sliderlabels[2][2].setText(str(bslider_value))
            if self.widgets.sliders[2].value() > bslider_value:
                self.widgets.sliders[2].setValue(bslider_value)
    
    def change_aslider(self, value):
        self.widgets.sliders[3].setMinimum(value)
        self.widgets.sliderlabels[3][0].setText(str(value))
    
    def change_bslider(self, value):
        self.widgets.sliders[2].setMaximum(value)
        self.widgets.sliderlabels[2][2].setText(str(value))
        if self.widgets.sliders[2].value() > value:
            self.widgets.sliders[2].setValue(value)

    def save_changes(self, main):
        for i, key in enumerate(['n', 'k', 'a','b']):
            main.data[key]=self.widgets.sliders[i].value()

        main.data['computer']=self.widgets.play_computer.isChecked()
        main.data['computer_turn']=self.widgets.play_computer_turn.isChecked()
        main.data['difficulty'] = int(self.widgets.difficulty_combo.currentText())
        main.data['gamemode'] = self.widgets.modes.index(self.widgets.mode_group.checkedButton())
        
        self.widgets.update_sticks(main.data['n'])
        
        main.dump()
        main.updateScreen('Start')

    def cancel_changes(self, main):
        for i, key in enumerate(['n', 'k', 'a','b']):
            self.widgets.sliders[i].setValue(main.data[key])

        self.widgets.sliderlabels[1][2].setText(str(main.data['n']))
        self.widgets.sliderlabels[2][2].setText(str(main.data['b']))
        self.widgets.sliderlabels[3][0].setText(str(main.data['a']))
        self.widgets.sliderlabels[3][2].setText(str(main.data['n']))

        self.widgets.play_computer.setChecked(main.data['computer'])
        self.widgets.play_computer_turn.setChecked(main.data['computer_turn'])
        self.widgets.difficulty_combo.setEnabled(main.data['computer'])
        self.widgets.play_computer_turn.setEnabled(main.data['computer'])
        self.widgets.difficulty_combo.setCurrentText(f"{main.data['difficulty']}")
        self.widgets.modes[main.data['gamemode']].setChecked(1)

        main.updateScreen('Start')
    
    def subscribe(self, main):
        self.widgets.ok.clicked.connect(lambda: self.save_changes(main))
        self.widgets.cancel.clicked.connect(lambda: self.cancel_changes(main))
        self.widgets.play_computer.stateChanged.connect(lambda state: self.widgets.difficulty_combo.setEnabled(state == Qt.Checked))
        self.widgets.play_computer.stateChanged.connect(lambda state: self.widgets.play_computer_turn.setEnabled(state == Qt.Checked))

        for i,slider in enumerate(self.widgets.sliders):
            slider.valueChanged.connect(lambda value, index_=i: self.widgets.sliderlabels[index_][1].setText(str(value)))
        self.widgets.sliders[0].valueChanged.connect(lambda value: self.change_nslider(value))
        self.widgets.sliders[2].valueChanged.connect(lambda value: self.change_aslider(value))
        self.widgets.sliders[3].valueChanged.connect(lambda value: self.change_bslider(value))