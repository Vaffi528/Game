from .package import *

#disable space button
class QPushButton(QPushButton):
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            event.ignore()
        else:
            super().keyPressEvent(event)

class SharedWidgets():
    def __init__(self, **kwargs):
        #style
        self.font = QtGui.QFont("monospace", 12)
        self.sticks_style = Path('style/stickbutton.css').read_text()

        #create push buttons
        ##greet
        self.play = QPushButton("Play")
        self.settings = QPushButton("Settings")
        self.info = QPushButton("Info")
        self.exit = QPushButton("Exit")
        ##settings
        self.ok = QPushButton("Ok")
        self.cancel = QPushButton("Cancel")
        ##play
        self.pause = QPushButton("||")
        self.pause.setAutoDefault(False)
        self.pause.setDefault(False)
        self.sticks = []
        for i in range(50):
            btn = QPushButton()
            btn.setStyleSheet(self.sticks_style)
            btn.setAutoDefault(False)
            btn.setDefault(False)
            if i > kwargs['n']-1:
                btn.hide()
            self.sticks.append(btn)
        self.next = QPushButton('Next')
        self.next.setDisabled(1)
        ##pause
        self.continue_ = QPushButton("Continue")
        self.endgame = QPushButton("End Game")
        ##end
        self.quit = QPushButton("Quit")


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
        ##play
        self.queue = QLabel("1 Player turn")
        ##end
        self.winner = QLabel()

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
        ##play
        self.pause.setStyleSheet("font-size: 16px;")
        self.next.setFont(QtGui.QFont("monospace", 20))
        self.queue.setFont(QtGui.QFont("monospace", 18))
        ##pause
        self.continue_.setFont(self.font)
        self.endgame.setFont(self.font)
        ##end
        self.quit.setFont(self.font)
        self.winner.setFont(QtGui.QFont("monospace", 28))

        #shortcuts
        ##greet
        self.exit_short = QAction('Exit')
        self.exit_short.setShortcut('Esc')
        ##play
        self.pause_short = QAction('Pause')
        self.pause_short.setShortcut('Esc')
        self.next_short = QAction('Next')
        self.next_short.setShortcut('Space')
        ##pause
        self.end_short = QAction('End')
        self.end_short.setShortcut('Esc')
        self.continue_short = QAction('Continue')
        self.continue_short.setShortcut('Space')
        ##quit
        self.quit_short = QAction('Quit')
        self.quit_short.setShortcut('Esc')

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

    # this method is calling in initialization and in case of updating "n" value (by ok button), interrrupting game (by end game button) or ending the game 
    def update_sticks(self, n):
        for i in range(50): 
            self.sticks[i].show()
            self.sticks[i].setDisabled(0)

        for i in range(49,n-1,-1): 
            self.sticks[i].hide()
        