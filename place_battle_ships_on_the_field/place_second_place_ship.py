from random import randint
from place_battle_ships_on_the_field.place_third_place_ship import matrix

row = randint(1, 11)
column = randint(1, 11)


def wrapper(matrix, row, column):
    matrix[row - 1][column] = 0
    matrix[row + 1][column] = 0
    matrix[row][column + 1] = 0
    matrix[row][column - 1] = 0
    matrix[row - 1][column - 1] = 0
    matrix[row - 1][column + 1] = 0
    matrix[row + 1][column - 1] = 0
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
    row_or_column = 2
    row, column = randint(1, 11), randint(1, 11)
    print(row, column)
    row, column = right_cell(row, column, i)
    if row_or_column == 1:
        row2 = choice([row - 1, row + 1])
        if matrix[row2][column] == '':
            matrix[row2][column] = i
        else:
            while matrix[row2][column] != '':
                row2 = choice([row - 1, row + 1])
            if matrix[row2][column] == '':
                matrix[row2][column] = i
        matrix[row2][column + 1] = 0
        matrix[row2][column - 1] = 0
        matrix[row][column + 1] = 0
        matrix[row][column - 1] = 0
        if row < row2:
            matrix[row2 + 1][column] = 0
            matrix[row2 - 2][column] = 0

            matrix[row2 + 1][column - 1] = 0
            matrix[row2 - 2][column - 1] = 0
            matrix[row2 + 1][column + 1] = 0
            matrix[row2 - 2][column + 1] = 0
        else:
            matrix[row + 1][column] = 0
            matrix[row - 2][column] = 0

            matrix[row + 1][column - 1] = 0
            matrix[row - 2][column - 1] = 0
            matrix[row + 1][column + 1] = 0
            matrix[row - 2][column + 1] = 0
    elif row_or_column == 2:
        column2 = choice([column - 1, column + 1])
        if matrix[row][column2] == '':
            matrix[row][column2] = i
        else:
            while matrix[row][column2] != '':
                column2 = choice([column - 1, column + 1])
            if matrix[row][column2] == '':
                matrix[row][column2] = i
        matrix[row + 1][column] = 0
        matrix[row - 1][column] = 0
        matrix[row + 1][column2] = 0
        matrix[row - 1][column2] = 0
        if column < column2:
            matrix[row][column2 + 1] = 0
            matrix[row][column - 1] = 0
        else:
            matrix[row][column + 1] = 0
            matrix[row][column2 - 1] = 0

        if str(matrix[row + 1][column2 - 1]) in "'', 0":
            matrix[row + 1][column2 - 1] = 0
        if str(matrix[row - 1][column2 - 1]) in "'', 0":
            matrix[row - 1][column2 - 1] = 0
        if str(matrix[row - 1][column2 + 1]) in "'', 0":
            matrix[row - 1][column2 + 1] = 0
        if str(matrix[row + 1][column2 + 1]) in "'', 0":
            matrix[row + 1][column2 + 1] = 0

        if str(matrix[row + 1][column - 1]) in "'', 0":
            matrix[row + 1][column - 1] = 0
        if str(matrix[row - 1][column - 1]) in "'', 0":
            matrix[row - 1][column - 1] = 0
        if str(matrix[row - 1][column + 1]) in "'', 0":
            matrix[row - 1][column + 1] = 0
        if str(matrix[row + 1][column + 1]) in "'', 0":
            matrix[row + 1][column + 1] = 0

if __name__ == '__main__':
    print(*matrix, sep="\n")

