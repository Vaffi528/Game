from random import randint

class Rule1Mode:
    def rule_logic(playscreen, main, ind=0):
        playscreen.picked_stickes += 1
        playscreen.total_quantity += 1
        if playscreen.total_quantity == main.data['n']:
            playscreen.reset(main)
            return
        if not playscreen.widgets.next.isEnabled():
            playscreen.widgets.next.setDisabled(0)
        if playscreen.picked_stickes == main.data['k']:
            Rule1Mode.update_turn_data(playscreen, main)
            
    def update_turn_data(playscreen, main=None, fl=False):
        playscreen.turn = not playscreen.turn
        playscreen.widgets.queue.setText(f'{playscreen.turn+1} Player turn')
        playscreen.widgets.next.setDisabled(1)
        playscreen.picked_stickes = 0
        if main:
            playscreen.subscribe_computer(main)

    def mode(all_sticks: list, playscreen, main, c) -> None:
        r = main.data['n']
        k = main.data['k']

        for stick in all_sticks:
            if not stick.isEnabled():
                r -= 1
        if c == 1:
            sticks = randint(1,k) if r % (k+1) == 0 else r % (k+1)
        else:
            adjustment = {8:0, 7:1, 6:2, 5:3, 4:3, 3:4, 2:4, 1:4, 0:4}
            chance = randint(1, 10 - adjustment[main.data['n']//(k+1)])

            sticks = randint(1,k) if (r % (k+1) == 0 or chance in range(1, c+1)) else r % (k+1)

        for stick in all_sticks:
            if stick.isEnabled():
                stick.setDisabled(1)
                sticks -= 1
                playscreen.total_quantity += 1
                if main.data['n'] == playscreen.total_quantity:
                    playscreen.reset(main)
                    return
            if sticks == 0:
                Rule1Mode.update_turn_data(playscreen)
                return 
    
