import sys
sys.path.append('.')
from tkinter import Tk, Button, Label, DISABLED
from clear_variant.clear_variant_for_computer import matrix as matrix_of_computer
from users_field.output_field import change_color
from functions.function import *


def print_real(matrix_of_user):
    for i in range(1, 11):
        for j in range(1, 11):
            if matrix_of_user[i][j] == 0:
                exec(f'btn{i}_{j}.config(text="•", fg="black", font="Arial 14", width=3, height=1)')
            elif matrix_of_user[i][j] == '':
                exec(f'btn{i}_{j}.config(text="")')


def change_color(btn, i, j):
    global dict_for_buttons
    global matrix_of_user
    global btn_wrapper
    if btn in dict_for_buttons and matrix_of_user[i][j] != 0:
        if dict_for_buttons[btn] == 0:
            btn.config(text='X', font="Arial 14", width=3, height=1, fg='black')
            dict_for_buttons[btn] = 1
            matrix_of_user[i][j] = 1

            btn_wrapper[btn] = []
            btn_wrapper[btn].append((i + 1, j - 1))
            btn_wrapper[btn].append((i - 1, j + 1))
            btn_wrapper[btn].append((i + 1, j + 1))
            btn_wrapper[btn].append((i - 1, j - 1))

            if i + 1 < 12 and j - 1 > -1 and matrix_of_user[i + 1][j - 1] == '':
                matrix_of_user[i + 1][j - 1] = 0
            if i - 1 > -1 and j + 1 < 12 and matrix_of_user[i - 1][j + 1] == '':
                matrix_of_user[i - 1][j + 1] = 0
            if i + 1 < 12 and j + 1 < 12 and matrix_of_user[i + 1][j + 1] == '':
                matrix_of_user[i + 1][j + 1] = 0
            if i - 1 > -1 and j - 1 > -1 and matrix_of_user[i - 1][j - 1] == '':
                matrix_of_user[i - 1][j - 1] = 0
        else:
            btn.config(text='')
            dict_for_buttons[btn] = 0
            matrix_of_user[i][j] = ''
            for i in btn_wrapper[btn]:
                flag = True
                val = btn_wrapper.values()
                for j in val:
                    if j != btn_wrapper[btn]:
                        if i in j:
                            flag = False
                            break
                if flag:
                    matrix_of_user[i[0]][i[1]] = ''
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
                    if matrix_of_user[i][j] == 0:
                        if str(matrix_of_user[i + 1][j]) in '0""' and str(matrix_of_user[i - 1][j]) in '0""':
                            if str(matrix_of_user[i][j + 1]) in '0""' and str(matrix_of_user[i][j - 1]) in '0""':
                                if str(matrix_of_user[i + 1][j + 1]) in '0""' and str(matrix_of_user[i + 1][j - 1]) in '0""':
                                    if str(matrix_of_user[i - 1][j + 1]) in '0""' and str(matrix_of_user[i - 1][j - 1]) in '0""':
                                        matrix_of_user[i][j] = ''
            btn_wrapper.pop(btn)
    else:
        if matrix_of_user[i][j] != 0:
            dict_for_buttons[btn] = 1
            btn.config(text='X', font="Arial 14", width=3, height=1, fg='black')
            btn_wrapper[btn] = []
            btn_wrapper[btn].append((i + 1, j - 1))
            btn_wrapper[btn].append((i - 1, j + 1))
            btn_wrapper[btn].append((i + 1, j + 1))
            btn_wrapper[btn].append((i - 1, j - 1))

            if i + 1 < 12 and j - 1 > -1 and matrix_of_user[i + 1][j - 1] == '':
                matrix_of_user[i + 1][j - 1] = 0
            if i - 1 > -1 and j + 1 < 12 and matrix_of_user[i - 1][j + 1] == '':
                matrix_of_user[i - 1][j + 1] = 0
            if i + 1 < 12 and j + 1 < 12 and matrix_of_user[i + 1][j + 1] == '':
                matrix_of_user[i + 1][j + 1] = 0
            if i - 1 > -1 and j - 1 > -1 and matrix_of_user[i - 1][j - 1] == '':
                matrix_of_user[i - 1][j - 1] = 0
            matrix_of_user[i][j] = 1
    print_real(matrix_of_user)


dict_for_buttons = {}
btn_wrapper = {}
matrix_of_user = [['' for j in range(12)] for i in range(12)]

window = Tk()
window.geometry('1100x700+150+50')
window.resizable(False, False)
window.title('Sea battle')

Label(window, text='Поле игрока', font="Arial 15").grid(row=0, column=0, columnspan=11)
Label(window, text='Поле компьютера', font="Arial 15").grid(row=0, column=13, columnspan=11)


def color(btnij, i, j, when_change_color):
    global matrix_of_computer
    btnij.config(text='', state='disabled')
    if matrix_of_computer[i][j] == when_change_color:
        btnij.config(bg='red')
    else:
        btnij.config(bg='blue')


alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    exec(f'''lbl{i} = Label(window, text=alphabet[{i}], font="Arial 15")
lbl{i}.grid(row=1, column={i + 1})''')

for i in range(1, 11):
    exec(f'''lbl2{i} = Label(window, text=digits[{i - 1}], font="Arial 15")
lbl2{i}.grid(row={i + 1}, column=0)''')

for i in range(2, 12):
    for j in range(1, 11):
        exec(f'btn{i - 1}_{j} = Button(window, text=matrix_of_user[{i - 1}][{j}], width=3, height=1, font="Arial 14", bg="white", fg="black", activebackground="blue", activeforeground="white", command = lambda: change_color(btn{i - 1}_{j}, {i - 1}, {j}))')
        exec(f'btn{i - 1}_{j}.grid(row={i}, column={j})')


def play(matrix_of_user):
    if stopper(matrix_of_user):
        for i in range(1, 11):
            for j in range(1, 11):
                exec(f'btn{i}_{j}.config(state=DISABLED, fg="black", bg="white")')


btn_play = Button(window, text='Играть', width=10, height=1, font="Arial 14", command=lambda: play(matrix_of_user))
btn_play.grid(row=11, column=12)


for i in range(10):
    exec(f'''lbl{i} = Label(window, text=alphabet[{i}], font="Arial 15")
lbl{i}.grid(row=1, column={i + 14})''')

for i in range(1, 11):
    exec(f'''lbl2{i} = Label(window, text=digits[{i - 1}], font="Arial 15")
lbl2{i}.grid(row={i + 1}, column=13)''')

for i in range(2, 12):
    for j in range(1, 11):
        exec(f'btn{i - 1}_{j + 13} = Button(window, text=matrix_of_computer[{i - 1}][{j}], width=3, height=1, font="Arial 14", bg="white", fg="black", activebackground="blue", activeforeground="white", command=lambda: color(btn{i - 1}_{j + 13}, {i - 1}, {j}, {1}))')
        exec(f'btn{i - 1}_{j + 13}.grid(row={i}, column={j + 13})')

window.mainloop()
