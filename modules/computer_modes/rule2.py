from random import randint

class Rule2Mode:
    def rule_logic(playscreen, main, ind=0):
        playscreen.picked_stickes += 1
        playscreen.total_quantity += 1

        if playscreen.total_quantity == main.data['n']:
            playscreen.reset(main)
            return

        if playscreen.picked_stickes == main.data['a']:
            playscreen.widgets.next.setDisabled(0)
        if playscreen.picked_stickes == main.data['b']:
            Rule2Mode.update_turn_data(playscreen, main)
    
    def update_turn_data(playscreen, main, fl=True):
        playscreen.turn = not playscreen.turn
        playscreen.widgets.queue.setText(f'{playscreen.turn+1} Player turn')
        playscreen.widgets.next.setDisabled(1)
        playscreen.picked_stickes = 0
        if (main.data['n'] - playscreen.total_quantity) < main.data['a']:
            playscreen.turn = not playscreen.turn
            playscreen.reset(main)
            return
        if fl:
            playscreen.subscribe_computer(main)

    def mode(all_sticks: list, playscreen, main, c) -> None:
        r = main.data['n']
        a = main.data['a']
        b = main.data['b']

        for stick in all_sticks:
            if not stick.isEnabled():
                r -= 1
        
        remainder = (r % (a+b))
        if remainder < a:
            sticks = a 
            if remainder == 0:
                sticks = randint(a,b)
        elif remainder > b:
            sticks = b 
        else:
            sticks = remainder

        if c != 1:
            adjustment = {12:0, 11:0, 10:1, 9:1, 8:2, 7:2, 6:3, 5:3, 4:3, 3:4, 2:4, 1:4, 0:4}
            chance = randint(1, 10 - adjustment[main.data['n']//(a+b)])
            if chance in range(1, c+1):
                sticks = randint(a,b)

        for stick in all_sticks:
            if stick.isEnabled():
                stick.setDisabled(1)
                sticks -= 1
                playscreen.total_quantity += 1
                if main.data['n'] == playscreen.total_quantity:
                    playscreen.reset(main)
                    return
            if sticks == 0:
                Rule2Mode.update_turn_data(playscreen, main, False)
                return 