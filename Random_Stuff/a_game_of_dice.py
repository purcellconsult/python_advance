from random import randint
"""
   _____      ________                                _____  ________  .__
  /  _  \    /  _____/_____    _____   ____     _____/ ____\ \______ \ |__| ____  ____
 /  /_\  \  /   \  ___\__  \  /     \_/ __ \   /  _ \   __\   |    |  \|  |/ ___\/ __ \
/    |    \ \    \_\  \/ __ \|        \  ___/  (  <_> )  |     |    `   \  \  \__\  ___/
\____|__  /  \______  (____  /__|_|  /\___  >  \____/|__|    /_______  /__|\___  >___  >
        \/          \/     \/      \/     \/                         \/        \/    \/
"""


def game(chances=10):
    for x in range(chances):
        dice = randint(1, 6)
        guess = int(input('Enter in a number '))
        print('Dice landed on {}'.format(dice))
        if dice == guess:
            print('You win')
        else:
            print('You lose :(')


game()