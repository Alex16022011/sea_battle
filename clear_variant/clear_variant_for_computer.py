import sys
sys.path.append('.')

from place_battle_ships_on_the_field.place_first_place_ship import matrix
from place_battle_ships_on_the_field.place_second_place_ship import matrix
from place_battle_ships_on_the_field.place_third_place_ship import matrix
from place_battle_ships_on_the_field.place_fourth_place_ship import matrix


for i in range(12):
    for j in range(12):
        if matrix[i][j] == '':
            matrix[i][j] = 0
        if str(matrix[i][j]) not in '0""':
            matrix[i][j] = 1
