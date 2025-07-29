from random import randint
class Rule1Mode:
    def mode1(all_sticks: list, playscreen, main) -> None:
        r = main.data['n']
        k = main.data['k']

        for stick in all_sticks:
            if not stick.isEnabled():
                r -= 1
        
        sticks = randint(1,k) if r % (k+1) == 0 else r % (k+1)
        
        for stick in all_sticks:
            if stick.isEnabled():
                stick.setDisabled(1)
                sticks -= 1
                playscreen.total_quantity += 1
                if main.data['n'] == playscreen.total_quantity:
                    playscreen.reset(main)
            if sticks == 0:
                playscreen.update_turn_data()
                return 