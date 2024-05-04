from tkinter import Tk, Button, Label
window = Tk()
window.geometry('750x550+250+50')
window.resizable(False, False)


def print_real():
    global matrix
    for i in range(2, 12):
        for j in range(2, 12):
            if matrix[i][j] == 0:
                exec(f'btn{i}{j}.config(text="•", fg="blue", font="Arial 9 bold")')
            elif matrix[i][j] == '':
                exec(f'btn{i}{j}.config(text="")')


def change_color(btn, i, j):
    global dict_for_buttons
    global matrix
    global btn_wrapper
    if btn in dict_for_buttons and matrix[i][j] != 0:
        if dict_for_buttons[btn] == 0:
            btn.config(text='X', font='Arial 9 bold', fg='blue')
            dict_for_buttons[btn] = 1
            exec(f'matrix[{i}][{j}] = 1')

            btn_wrapper[btn] = []
            if f'matrix[{i + 1}][{j - 1}]' == '':
                btn_wrapper[btn].append((i + 1, j - 1))
            if f'matrix[{i - 1}][{j + 1}]' == '':
                btn_wrapper[btn].append((i - 1, j + 1))
            if f'matrix[{i + 1}][{j + 1}]' == '':
                btn_wrapper[btn].append((i + 1, j + 1))
            if f'matrix[{i - 1}][{j - 1}]' == '':
                btn_wrapper[btn].append((i - 1, j - 1))
            print(btn_wrapper[btn])

            if i + 1 < 12 and j - 1 > -1 and matrix[i][j] == '':
                matrix[i + 1][j - 1] = 0
            if i - 1 > -1 and j + 1 < 12 and matrix[i][j] == '':
                matrix[i - 1][j + 1] = 0
            if i + 1 < 12 and j + 1 < 12 and matrix[i][j] == '':
                matrix[i + 1][j + 1] = 0
            if i - 1 > -1 and j - 1 > -1 and matrix[i][j] == '':
                matrix[i - 1][j - 1] = 0
            print_real()
        else:
            btn.config(text='')
            dict_for_buttons[btn] = 0
            exec(f"matrix[{i}][{j}] = ''")

            # if i + 1 < 12 and j - 1 > -1:
            #     matrix[i + 1][j - 1] = ''
            # if i - 1 > -1 and j + 1 < 12:
            #     matrix[i - 1][j + 1] = ''
            # if i + 1 < 12 and j + 1 < 12:
            #     matrix[i + 1][j + 1] = ''
            # if i - 1 > -1 and j - 1 > -1:
            #     matrix[i - 1][j - 1] = ''
            print(btn_wrapper[btn])
            for i in btn_wrapper[btn]:
                exec(f"matrix[{i[0]}][{i[1]}] = ''")
                print(f"matrix[{i[0]}][{i[1]}] = ''")
            print_real()
            btn_wrapper.pop(btn)
    else:
        if matrix[i][j] != 0:
            dict_for_buttons[btn] = 1
            btn.config(text='X', font='Arial 9 bold', fg='blue')
            btn_wrapper[btn] = []
            if f'matrix[{i + 1}][{j - 1}]' == '':
                btn_wrapper[btn].append((i + 1, j - 1))
            if f'matrix[{i - 1}][{j + 1}]' == '':
                btn_wrapper[btn].append((i - 1, j + 1))
            if f'matrix[{i + 1}][{j + 1}]' == '':
                btn_wrapper[btn].append((i + 1, j + 1))
            if f'matrix[{i - 1}][{j - 1}]' == '':
                btn_wrapper[btn].append((i - 1, j - 1))
            print(btn_wrapper[btn])


            if i + 1 < 12 and j - 1 > -1 and matrix[i][j] == '':
                matrix[i + 1][j - 1] = 0
            if i - 1 > -1 and j + 1 < 12 and matrix[i][j] == '':
                matrix[i - 1][j + 1] = 0
            if i + 1 < 12 and j + 1 < 12 and matrix[i][j] == '':
                matrix[i + 1][j + 1] = 0
            if i - 1 > -1 and j - 1 > -1 and matrix[i][j] == '':
                matrix[i - 1][j - 1] = 0
            exec(f'matrix[{i}][{j}] = 1')
            print_real()
    
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
        exec(f'''btn{i + 1}{j + 1} = Button(window, bg="white", fg="blue", width=5, height=2, activeforeground="blue", activebackground="white",
            bd=3, command=lambda: change_color(btn{i + 1}{j + 1}, {i + 1}, {j + 1}))
btn{i + 1}{j + 1}.grid(row={i},column={j}, padx=1, pady=1)''')

window.mainloop()