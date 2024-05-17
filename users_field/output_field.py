import sys
sys.path.append('.')
from functions.function import *
from tkinter import Tk, Button, Label
window = Tk()
window.geometry('800x550+250+50')
window.resizable(False, False)
btn = Button(text='Отправить', command=lambda: play(matrix))

def print_real(matrix):
    for i in range(1, 11):
        for j in range(1, 11):
            if matrix[i][j] == 0:
                exec(f'btn{i}{j}.config(text="•", fg="blue", font="Arial 9 bold")')
            elif matrix[i][j] == '':
                exec(f'btn{i}{j}.config(text="")')

def change_color(btn, i, j):
    global dict_for_buttons
    global matrix
    global btn_wrapper
    print('до:', *matrix, sep='\n')
    if btn in dict_for_buttons and matrix[i][j] != 0:
        if dict_for_buttons[btn] == 0:
            btn.config(text='X', font='Arial 9 bold', fg='blue')
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
            btn.config(text='X', font='Arial 9 bold', fg='blue')
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
    matrix = stopper(matrix)
    print_real(matrix)
    print('после:', *matrix, sep='\n')
    
dict_for_buttons = {}
btn_wrapper = {}
matrix = [['' for j in range(12)] for i in range(12)]
alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


for i in range(10):
    exec(f'''lbl{i} = Label(window, text=alphabet[{i}], font="Arial 15")
lbl{i}.grid(row=0, column={i + 1})''')
    
for i in range(10):
    exec(f'''lbl2{i} = Label(window, text=digits[{i}], font="Arial 15")
lbl2{i}.grid(row={i + 1}, column=0)''')
    
for i in range(1, 11):
    for j in range(1, 11):
        exec(f'''btn{i}{j} = Button(window, bg="white", fg="blue", width=5, height=2, activeforeground="blue", activebackground="white",
            bd=3, command=lambda: change_color(btn{i}{j}, {i}, {j}))
btn{i}{j}.grid(row={i},column={j}, padx=1, pady=1)''')

window.mainloop()