from tkinter import Tk, Button, Label
window = Tk()
window.geometry('750x550+250+50')
window.resizable(False, False)


def wrapper(btn):
    global matrix
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                matrix[i + 1][j - 1] = 0
                matrix[i - 1][j + 1] = 0
                matrix[i + 1][j + 1] = 0
                matrix[i - 1][j - 1] = 0


def change_color(btn, i, j):
    global dict_for_buttons
    global matrix
    row_dict = {}
    column_dict = {}
    if btn in dict_for_buttons and matrix[i][j] != 0:
        if dict_for_buttons[btn] == 0:
            btn.config(text='X', font='Arial 9 bold', fg='blue')
            dict_for_buttons[btn] = 1
            row_dict[btn] = i
            column_dict[btn] = j
            exec(f'matrix[{i}][{j}] = 1')
        else:
            btn.config(text='')
            dict_for_buttons[btn] = 0
            row_dict[btn] = 0
            column_dict[btn] = 0
            exec(f'matrix[{i}][{j}] = 0')
    else:
        if matrix[i][j] != 0:
            dict_for_buttons[btn] = 1
            btn.config(text='X', font='Arial 9 bold', fg='blue')
            row_dict[btn] = i
            column_dict[btn] = j
            exec(f'matrix[{i}][{j}] = 1')
    wrapper(btn)
    
dict_for_buttons = {}
matrix = [['' for j in range(10)] for i in range(10)]
alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(10):
    exec(f'''lbl{i} = Label(window, text=alphabet[{i}], font="Arial 15")
lbl{i}.grid(row=0, column={i + 1})''')
    
for i in range(10):
    exec(f'''lbl2{i} = Label(window, text=digits[{i}], font="Arial 15")
lbl2{i}.grid(row={i + 1}, column=0)''')
    
for i in range(10):
    for j in range(10):
        exec(f'''btn{i}{j} = Button(window, bg="white", fg="blue", width=5, height=2, activeforeground="blue", activebackground="white",
            bd=3, command=lambda: change_color(btn{i}{j}, {i}, {j}))
btn{i}{j}.grid(row={i + 1},column={j + 1}, padx=1, pady=1)''')

window.mainloop()