import sys
sys.path.append('.')

from random import randint, choice
from place_battle_ships_on_the_field.place_third_place_ship import matrix
# from field_of_game.create_sea_battle_field import matrix
row = randint(1, 11)
column = randint(1, 11)


def wrapper(matrix, row, column):
    if 0 < row - 1 < 12 and -1 < column < 11:
        matrix[row - 1][column] = 0
    if -1 < row + 1 < 11 and -1 < column < 11:
        matrix[row + 1][column] = 0
    if -1 < row < 11 and -1 < column < 11:
        matrix[row][column + 1] = 0
    if -1 < row < 11 and 0 < column < 11:
        matrix[row][column - 1] = 0
    if 0 < row - 1 < 11 and 0 < column < 11:
        matrix[row - 1][column - 1] = 0
    if 0 < row - 1 < 11 and -1 < column < 11:
        matrix[row - 1][column + 1] = 0
    if -1 < row + 1 < 11 and 0 < column < 11:
        matrix[row + 1][column - 1] = 0
    if -1 < row + 1 < 11 and 0 < column < 11:
        matrix[row + 1][column + 1] = 0


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


for i in range(5, 8):
    row_or_column = choice(['row', 'column'])
    row, column = randint(1, 11), randint(1, 11)
    row, column = right_cell(row, column, i)
    if row_or_column == 'column':
        row2 = choice([row - 1, row + 1])
        if matrix[row2][column] != '':
            if row2 == row - 1:
                row2 = row + 1
            else:
                row2 = row - 1
        matrix[row2][column] = i

        if -1 < row < 11 and -1 < column < 11:
            matrix[row][column + 1] = 0
        if -1 < row2 < 11 and -1 < column < 11:
            matrix[row2][column + 1] = 0
        if -1 < row < 11 and 0 < column < 11:
            matrix[row][column - 1] = 0
        if -1 < row2 < 11 and 0 < column < 11:
            matrix[row2][column - 1] = 0

        if 0 < min(row, row2) - 1 < 11 and -1 < column < 11:
            matrix[min(row, row2) - 1][column] = 0
        if -1 < max(row, row2) + 1 < 11 and -1 < column < 11:
            matrix[max(row, row2) + 1][column] = 0

        if 0 < min(row, row2) - 1 < 11 and -1 < column + 1 < 11:
            matrix[min(row, row2) - 1][column + 1] = 0
        if -1 < max(row, row2) + 1 < 11 and -1 < column + 1 < 11:
            matrix[max(row, row2) + 1][column + 1] = 0

        if 0 < min(row, row2) - 1 < 11 and 0 < column - 1 < 11:
            matrix[min(row, row2) - 1][column - 1] = 0
        if -1 < max(row, row2) + 1 < 11 and 0 < column - 1 < 11:
            matrix[max(row, row2) + 1][column - 1] = 0

    elif row_or_column == 'row':
        column2 = choice([column - 1, column + 1])
        if matrix[row][column2] != '':
            if column2 == column - 1:
                column2 = column + 1
            else:
                column2 = column - 1
        matrix[row][column2] = i

        if -1 < row + 1 < 11 and -1 < column < 11:
            matrix[row + 1][column] = 0
        if -1 < row + 1 < 11 and -1 < column2 < 11:
            matrix[row + 1][column2] = 0
        if 0 < row - 1 < 11 and -1 < column < 11:
            matrix[row - 1][column] = 0
        if 0 < row - 1 < 11 and -1 < column2 < 11:
            matrix[row - 1][column2] = 0

        if -1 < row < 11 and 0 < min(column, column2) - 1 < 11:
            matrix[row][min(column, column2) - 1] = 0
        if -1 < row < 11 and 0 < max(column, column2) + 1 < 11:
            matrix[row][max(column, column2) + 1] = 0

        if -1 < row + 1 < 11 and 0 < min(column, column2) - 1 < 11:
            matrix[row + 1][min(column, column2) - 1] = 0
        if -1 < row + 1 < 11 and -1 < max(column, column2) + 1 < 11:
            matrix[row + 1][max(column, column2) + 1] = 0
        if 0 < row - 1 < 11 and 0 < min(column, column2) - 1 < 11:
            matrix[row - 1][min(column, column2) - 1] = 0
        if 0 < row - 1 < 11 and -1 < max(column, column2) + 1 - 1 < 11:
            matrix[row - 1][max(column, column2) + 1] = 0


if __name__ == '__main__':
    print(*matrix, sep="\n")

