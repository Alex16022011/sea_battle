import sys
sys.path.append('.')

from random import randint, choice
from place_battle_ships_on_the_field.place_fourth_place_ship import matrix
# from field_of_game.create_sea_battle_field import matrix
row = randint(1, 11)
column = randint(1, 11)


def right_cell(row, column, fill):
    if matrix[row][column] == '':
        matrix[row][column] = fill
    else:
        while matrix[row][column] != '':
            row = randint(1, 11)
            column = randint(1, 11)
        if matrix[row][column] == '':
            matrix[row][column] = fill
    return row, column


for i in range(8, 10):
    row_or_column = choice(['row', 'column'])
    row, column = randint(1, 11), randint(1, 11)
    print(row, column)
    row, column = right_cell(row, column, i)
    if row_or_column == 'column':
        row2 = choice([row - 1, row + 1])
        if matrix[row2][column] != '':
            if row2 == row - 1:
                row2 = row + 1
            else:
                row2 = row - 1
        matrix[row2][column] = i
        matrix[row2][column + 1] = 0
        matrix[row2][column - 1] = 0
        matrix[row][column + 1] = 0
        matrix[row][column - 1] = 0

        row3 = choice([min(row, row2) - 1, max(row, row2) + 1])
        if matrix[row3][column] != '':
            if row3 == min(row, row2) - 1:
                row3 = max(row, row2) + 1
            else:
                row3 = min(row, row2) - 1
        matrix[row3][column] = i

        matrix[row][column + 1] = 0
        matrix[row2][column + 1] = 0
        matrix[row3][column + 1] = 0

        matrix[row][column - 1] = 0
        matrix[row2][column - 1] = 0
        matrix[row3][column - 1] = 0

        matrix[min(row, row2, row3) - 1][column] = 0
        matrix[max(row, row2, row3) + 1][column] = 0

        matrix[min(row, row2, row3) - 1][column + 1] = 0
        matrix[max(row, row2, row3) + 1][column + 1] = 0
        matrix[min(row, row2, row3) - 1][column - 1] = 0
        matrix[max(row, row2, row3) + 1][column - 1] = 0
    elif row_or_column == 'row':
        column2 = choice([column - 1, column + 1])
        if matrix[row][column2] != '':
            if column2 == column - 1:
                column2 = column + 1
            else:
                column2 = column - 1
        matrix[row][column2] = i

        column3 = choice([min(column, column2) - 1, max(column, column2) + 1])
        if matrix[row][column3] != '':
            if column3 == min(column, column2) - 1:
                column3 = max(column, column2) + 1
            else:
                column3 = min(column, column2) - 1
        matrix[row][column3] = i

        matrix[row - 1][column] = 0
        matrix[row - 1][column2] = 0
        matrix[row - 1][column3] = 0

        matrix[row + 1][column] = 0
        matrix[row + 1][column2] = 0
        matrix[row + 1][column3] = 0

        matrix[row][min(column, column2, column3) - 1] = 0
        matrix[row][max(column, column2, column3) + 1] = 0

        matrix[row + 1][min(column, column2, column3) - 1] = 0
        matrix[row + 1][max(column, column2, column3) + 1] = 0
        matrix[row - 1][min(column, column2, column3) - 1] = 0
        matrix[row - 1][max(column, column2, column3) + 1] = 0


if __name__ == '__main__':
    print(*matrix, sep="\n")


