from random import choice

class Rule3Mode():
    def __init__(self):
        self.indleft = None
        self.indright = None
        self.turn = False
        self.self_turn = False
        self.index = None

    def rule_logic(self, playscreen, main, ind=0):
        if playscreen.picked_stickes > 0:
            if ind != self.indleft and ind != self.indright:
                playscreen.widgets.sticks[ind].setDisabled(0)
                return
        else:
            self.indleft = None
            self.indright = None
            if ind != 0 and playscreen.widgets.sticks[ind-1].isEnabled():
                self.indleft = ind-1
            if ind != main.data['n']-1 and playscreen.widgets.sticks[ind+1].isEnabled():
                self.indright = ind+1

        if ind == self.indleft:
            self.indleft = None
            if ind != 0 and playscreen.widgets.sticks[ind-1].isEnabled():
                self.indleft = ind-1

        elif ind == self.indright:
            self.indright = None
            if ind != main.data['n']-1 and playscreen.widgets.sticks[ind+1].isEnabled():
                self.indright = ind+1
        
        playscreen.picked_stickes += 1
        playscreen.total_quantity += 1

        if playscreen.total_quantity == main.data['n']:
            playscreen.reset(main)
            return
        if not playscreen.widgets.next.isEnabled():
            playscreen.widgets.next.setDisabled(0)
        if playscreen.picked_stickes == main.data['k'] or (self.indleft == None and self.indright == None):
            self.update_turn_data(playscreen, main)
            
    def update_turn_data(self, playscreen, main=None, fl=False):
        playscreen.turn = not playscreen.turn
        playscreen.widgets.queue.setText(f'{playscreen.turn+1} Player turn')
        playscreen.widgets.next.setDisabled(1)
        playscreen.picked_stickes = 0
        if main:
            playscreen.subscribe_computer(main)

    def mode(self, all_sticks: list, playscreen, main, c) -> None:
        r = main.data['n']
        k = main.data['k']
        gamefield = [stick.isEnabled() for stick in all_sticks]

        if all(el==1 for el in gamefield):
            self.symmetrical_choice(r, k, all_sticks, playscreen)

        elif self.self_turn:
            if self.index == None:
                disabled_list = self.xor_list(gamefield)
                inds = [i for i, value in enumerate(disabled_list) if value == 1]
                if all_sticks[inds[0]].isEnabled():
                    for i in inds:
                        all_sticks[i].setDisabled(1)
                        playscreen.total_quantity += 1
                else:
                    for i in inds:
                        all_sticks[-(i+1)].setDisabled(1)
                        playscreen.total_quantity += 1
            else:
                if self.index >= 0: disabled_list = self.xor_list(gamefield[self.index:]) 
                else: disabled_list = self.xor_list(gamefield[:self.index])

                inds = [i for i, value in enumerate(disabled_list) if value == 1]
                if self.index >= 0:
                    if all_sticks[inds[0]+self.index].isEnabled():
                        for i in inds:
                            all_sticks[i+self.index].setDisabled(1)
                            playscreen.total_quantity += 1
                    else:
                        for i in inds:
                            all_sticks[-(i+1)].setDisabled(1)
                            playscreen.total_quantity += 1
                else:
                    if all_sticks[inds[0]].isEnabled():
                        for i in inds:
                            all_sticks[i].setDisabled(1)
                            playscreen.total_quantity += 1
                    else:
                        for i in inds:
                            all_sticks[-(i+1+abs(self.index))].setDisabled(1)
                            playscreen.total_quantity += 1
            

        else:
            disabled_list = self.xor_list(gamefield)
            if all(el==False for el in disabled_list):
                pass
            elif disabled_list[0] == 1:
                self.index = max([i for i, value in enumerate(disabled_list) if value == 1])

                ind_max = max([i for i, value in enumerate(gamefield) if value == 1])
                ind_min = min([i for i, value in enumerate(gamefield) if value == 1])
                if len([el for el in gamefield if el == 1]) <= k and (all(el==1 for el in gamefield[ind_min+1:]) or 
                                                                        all(el==1 for el in gamefield[:ind_max+1])):
                    for stick in all_sticks:
                        if stick.isEnabled():
                            stick.setDisabled(1)
                            playscreen.total_quantity += 1
                    
                    self.reset(playscreen, main)

                elif not all_sticks[self.index].isEnabled():
                    self.symmetrical_choice(r-(self.index+1), k, all_sticks[self.index+1:], playscreen)
                    self.index = self.index+1
                else:
                    self.symmetrical_choice(r-(self.index+1), k, all_sticks[:-(self.index+1)], playscreen)
                    self.index = -(self.index+1)

            
        self.reset(playscreen, main)


    def reset(self, playscreen, main):
        if main.data['n'] == playscreen.total_quantity:
            self.self_turn = False
            playscreen.reset(main)
            return
        else:
            self.update_turn_data(playscreen)
            return
    
    def xor_list(self, gamefield) -> list:
        part1 = gamefield[:len(gamefield)//2]
        part2 = reversed(gamefield[len(gamefield)//2 + (1 if len(gamefield)%2==1 else 0):])
        disabled_list = [a ^ b for a, b in zip(part1, part2)]
        return disabled_list
    
    def symmetrical_choice(self, r, k, all_sticks, playscreen):
        if r % 2 == 0:
            rand = range(2, k+2 if k%2 == 0 else k+1, 2)
            sticks = choice(rand)
            for i in range(r//2-sticks//2,r//2+sticks//2):
                all_sticks[i].setDisabled(1)
                playscreen.total_quantity += 1
        else:
            rand = range(1, k+2 if k%2 == 1 else k+1, 2)
            sticks = choice(rand)
            for i in range(r//2-sticks//2,r//2+sticks//2+1):
                all_sticks[i].setDisabled(1)
                playscreen.total_quantity += 1

        self.self_turn = True
    
