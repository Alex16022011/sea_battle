import sys
sys.path.append('../main_logic')
from random import randint
from field_of_game.create_sea_battle_field import matrix

row = randint(1, 11)
column = randint(1, 11)



if __name__ == '__main__':
    print(*matrix, sep="\n")

