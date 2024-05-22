import sys
sys.path.append('.')

from random import randint, choice
from field_of_game.create_sea_battle_field import matrix
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


for i in range(10, 11):
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

        row3 = choice([min(row, row2) - 1, max(row, row2) + 1])
        if matrix[row3][column] != '':
            if row3 == min(row, row2) - 1:
                row3 = max(row, row2) + 1
            else:
                row3 = min(row, row2) - 1
        matrix[row3][column] = i

        row4 = choice([min(row, row2, row3) - 1, max(row, row2, row3) + 1])
        if matrix[row4][column] != '':
            if row4 == min(row, row2, row3) - 1:
                row4 = max(row, row2, row3) + 1
            else:
                row4 = min(row, row2, row3) - 1
        matrix[row4][column] = i

        if -1 < column + 1 < 11:
            matrix[row][column + 1] = 0
            matrix[row2][column + 1] = 0
            matrix[row3][column + 1] = 0
            matrix[row4][column + 1] = 0

        if 0 < column - 1 < 11:
            matrix[row][column - 1] = 0
            matrix[row2][column - 1] = 0
            matrix[row3][column - 1] = 0
            matrix[row4][column - 1] = 0

        if 0 < min(row, row2, row3, row4) - 1 < 11:
            matrix[min(row, row2, row3, row4) - 1][column] = 0
        if -1 < max(row, row2, row3, row4) + 1 < 11:
            matrix[max(row, row2, row3, row4) + 1][column] = 0

        if -1 < column + 1 < 11:
            if 0 < min(row, row2, row3, row4) - 1 < 11 :
                matrix[min(row, row2, row3, row4) - 1][column + 1] = 0
            if -1 < max(row, row2, row3, row4) + 1 < 11:
                matrix[max(row, row2, row3, row4) + 1][column + 1] = 0

        if 0 < column - 1 < 11:
            if 0 < min(row, row2, row3, row4) - 1 < 11:
                matrix[min(row, row2, row3, row4) - 1][column - 1] = 0
            if -1 < max(row, row2, row3, row4) + 1 < 11:
                matrix[max(row, row2, row3, row4) + 1][column - 1] = 0

    elif row_or_column == 'row':
        column2 = choice([column - 1, column + 1])
        if matrix[row][column2] != '':
            if column2 == column - 1:
                column2 = column + 1
            else:
                column2 = column - 1
        matrix[row][column2] = i

        if -1 < row + 1 < 11:
            matrix[row + 1][column] = 0
            matrix[row + 1][column2] = 0
        if 0 < row - 1 < 11:
            matrix[row - 1][column] = 0
            matrix[row - 1][column2] = 0

        column3 = choice([min(column, column2) - 1, max(column, column2) + 1])
        if matrix[row][column3] != '':
            if column3 == min(column, column2) - 1:
                column3 = max(column, column2) + 1
            else:
                column3 = min(column, column2) - 1
        matrix[row][column3] = i

        column4 = choice([min(column, column2, column3) - 1, max(column, column2, column3) + 1])
        if matrix[row][column4] != '':
            if column4 == min(column, column2, column3) - 1:
                column4 = max(column, column2, column3) + 1
            else:
                column4 = min(column, column2, column3) - 1
        matrix[row][column4] = i

        if -1 < row + 1 < 11:
            matrix[row + 1][column3] = 0
            matrix[row + 1][column4] = 0
        if 0 < row - 1 < 11:
            matrix[row - 1][column3] = 0
            matrix[row - 1][column4] = 0
        if 0 < min(column, column2, column3, column4) - 1 < 11:
            matrix[row][min(column, column2, column3, column4) - 1] = 0
        if -1 < max(column, column2, column3, column4) + 1 < 11:
            matrix[row][max(column, column2, column3, column4) + 1] = 0

        if -1 < row + 1 < 11:
            if 0 < min(column, column2, column3, column4) - 1 < 11:
                matrix[row + 1][min(column, column2, column3, column4) - 1] = 0
            if -1 < max(column, column2, column3, column4) + 1 < 11:
                matrix[row + 1][max(column, column2, column3, column4) + 1] = 0

        if 0 < row - 1 < 11:
            if 0 < min(column, column2, column3, column4) - 1 < 11:
                matrix[row - 1][min(column, column2, column3, column4) - 1] = 0
            if -1 < max(column, column2, column3, column4) + 1 < 11:
                matrix[row - 1][max(column, column2, column3, column4) + 1] = 0


if __name__ == '__main__':
    print(*matrix, sep="\n")


