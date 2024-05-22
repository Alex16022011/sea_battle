import sys
sys.path.append('.')
from functions.function import *


def print_real(matrix):
    for i in range(1, 11):
        for j in range(1, 11):
            if matrix[i][j] == 0:
                exec(f'btn{i}_{j}.config(text="•", fg="blue", font="Arial 14 bold", width=3, height=1)')
            elif matrix[i][j] == '':
                exec(f'btn{i}_{j}.config(text="")')


def change_color(btn, i, j):
    global dict_for_buttons
    global matrix
    global btn_wrapper
    if btn in dict_for_buttons and matrix[i][j] != 0:
        if dict_for_buttons[btn] == 0:
            btn.config(text='X', font="Arial 14 bold", width=3, height=1, fg='blue')
            dict_for_buttons[btn] = 1
            matrix[i][j] = 1

            btn_wrapper[btn] = []
            btn_wrapper[btn].append((i + 1, j - 1))
            btn_wrapper[btn].append((i - 1, j + 1))
            btn_wrapper[btn].append((i + 1, j + 1))
            btn_wrapper[btn].append((i - 1, j - 1))

            if i + 1 < 12 and j - 1 > -1 and matrix[i + 1][j - 1] == '':
                matrix[i + 1][j - 1] = 0
            if i - 1 > -1 and j + 1 < 12 and matrix[i - 1][j + 1] == '':
                matrix[i - 1][j + 1] = 0
            if i + 1 < 12 and j + 1 < 12 and matrix[i + 1][j + 1] == '':
                matrix[i + 1][j + 1] = 0
            if i - 1 > -1 and j - 1 > -1 and matrix[i - 1][j - 1] == '':
                matrix[i - 1][j - 1] = 0
        else:
            btn.config(text='')
            dict_for_buttons[btn] = 0
            matrix[i][j] = ''
            for i in btn_wrapper[btn]:
                flag = True
                val = btn_wrapper.values()
                for j in val:
                    if j != btn_wrapper[btn]:
                        if i in j:
                            flag = False
                            break
                if flag:
                    matrix[i[0]][i[1]] = ''
                    # if i[1] - i[0] == 4:
                    #     fourth_ship += 1
                    # elif i[1] - i[0] == 3:
                    #     third_ship += 1
                    # elif i[1] - i[0] == 2:
                    #     second_ship += 1
                    # elif i[1] - i[0] == 1:
                    #     first_ship += 1
            for i in range(11):
                for j in range(11):
                    if matrix[i][j] == 0:
                        if str(matrix[i + 1][j]) in '0""' and str(matrix[i - 1][j]) in '0""':
                            if str(matrix[i][j + 1]) in '0""' and str(matrix[i][j - 1]) in '0""':
                                if str(matrix[i + 1][j + 1]) in '0""' and str(matrix[i + 1][j - 1]) in '0""':
                                    if str(matrix[i - 1][j + 1]) in '0""' and str(matrix[i - 1][j - 1]) in '0""':
                                        matrix[i][j] = ''
            btn_wrapper.pop(btn)
    else:
        if matrix[i][j] != 0:
            dict_for_buttons[btn] = 1
            btn.config(text='X', font="Arial 14 bold", width=3, height=1, fg='blue')
            btn_wrapper[btn] = []
            btn_wrapper[btn].append((i + 1, j - 1))
            btn_wrapper[btn].append((i - 1, j + 1))
            btn_wrapper[btn].append((i + 1, j + 1))
            btn_wrapper[btn].append((i - 1, j - 1))

            if i + 1 < 12 and j - 1 > -1 and matrix[i + 1][j - 1] == '':
                matrix[i + 1][j - 1] = 0
            if i - 1 > -1 and j + 1 < 12 and matrix[i - 1][j + 1] == '':
                matrix[i - 1][j + 1] = 0
            if i + 1 < 12 and j + 1 < 12 and matrix[i + 1][j + 1] == '':
                matrix[i + 1][j + 1] = 0
            if i - 1 > -1 and j - 1 > -1 and matrix[i - 1][j - 1] == '':
                matrix[i - 1][j - 1] = 0
            matrix[i][j] = 1
    print_real(matrix)


dict_for_buttons = {}
btn_wrapper = {}
matrix = [['' for j in range(12)] for i in range(12)]
