from .package import *

class SharedWidgets():
    def __init__(self, **kwargs):
        #font
        self.font = QtGui.QFont("monospace", 12)

        #create push buttons
        ##greet
        self.play = QPushButton("Play")
        self.settings = QPushButton("Settings")
        self.info = QPushButton("Info")
        self.exit = QPushButton("Exit")
        ##settings
        self.ok = QPushButton("Ok")
        self.cancel = QPushButton("Cancel")

        #create check boxes 
        ##settings
        self.play_computer = QCheckBox("Play against the computer")
        self.play_computer.setChecked(kwargs['computer'])
        #create sliders
        ##settings
        self.sliders = [self.create_slider(5,50,kwargs['n']),
                        self.create_slider(5,kwargs['n'],kwargs['k']),
                        self.create_slider(2,kwargs['b'],kwargs['a']),
                        self.create_slider(kwargs['a'],kwargs['n'],kwargs['b'])]
        #create labels
        ##settings
        self.difficulty_lvl = QLabel("Level of difficulty")
        self.game_rules = QLabel("Game rules (modes):")
        self.sliderlabels = [self.create_labels_for_sliders(5,50,kwargs['n'],'Amount of the sticks'),
                            self.create_labels_for_sliders(5,kwargs['n'],kwargs['k'],'Max amount of sticks for one pick'),
                            self.create_labels_for_sliders(2,kwargs['b'],kwargs['a'],'Min amount of sticks in for one pick in a row'),
                            self.create_labels_for_sliders(kwargs['a'],kwargs['n'],kwargs['b'],'Max amount of sticks in for one pick in a row')]
        #create combo boxes
        ##settings
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems([str(i) for i in range(1, 6)])
        self.difficulty_combo.setCurrentText(f"{kwargs['difficulty']}")
        self.difficulty_combo.setEnabled(kwargs['computer'])

        #create radio buttons
        ##settings
        self.mode_group = QButtonGroup()
        self.modes = [
            QRadioButton('''Стандартно: За ход можно взять от 1 до 𝑘 (включительно) любых палочек. 
                Брать можно любые палочки (необязательно подряд).'''),
            QRadioButton('''Интервальный выбор: За ход можно взять от 𝑎 до 𝑏 (включительно) любых палочек.'''),
            QRadioButton('''Подряд: За ход можно взять от 1 до 𝑘 подряд идущих палочек (никаких пропусков, только связный фрагмент,
            например, если палочки лежат как ||| ||, то взять 4 палочки не получится: тут изображено пустое пространство после
            третьей палочки, то есть палочку после третьей взяли на одном из предыдущих ходов).'''),
            QRadioButton('''Подряд и интервально: За ход можно взять от 𝑎 до 𝑏 подряд идущих палочек.'''),
            QRadioButton('''Особое: За ход разрешается взять либо 3 подряд идущих палочки, либо 1 любую палочку, либо 2 любые палочки.'''),
        ]
        
        for button in self.modes:
            #font of buttons
            button.setFont(self.font)
            self.mode_group.addButton(button)
        
        self.modes[kwargs['gamemode']].setChecked(1)

        #set style
        ##greet
        self.play.setFont(self.font)
        self.settings.setFont(self.font)
        self.info.setFont(self.font)
        self.exit.setFont(self.font)
        ##settings
        self.play_computer.setFont(self.font)
        self.difficulty_lvl.setFont(self.font)
        self.difficulty_combo.setFont(self.font)
        self.game_rules.setFont(self.font)
        for labels in self.sliderlabels:
            for label in labels:
                label.setFont(self.font)
        self.ok.setFont(self.font)
        self.cancel.setFont(self.font)

    def create_slider(self, min_val, max_val, curr_val) -> QSlider:
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setPageStep(1)
        slider.setProperty("value", curr_val)
        return slider
    
    def create_labels_for_sliders(self, min_val, max_val, curr_val, text) -> list[QLabel]:
        minlabel = QLabel(f'{min_val}')
        currlabel = QLabel(f'{curr_val}')
        maxlabel = QLabel(f'{max_val}')
        titlelabel = QLabel(f'{text}')
        return [minlabel, currlabel, maxlabel, titlelabel]
