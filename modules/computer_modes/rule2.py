from random import randint

class Rule2Mode:
    def rule_logic(playscreen, main):
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
        elif remainder > b:
            sticks = b 
        else:
            sticks = remainder

        if c != 1:
            chance = randint(c-1,7)
            if chance == 7:
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