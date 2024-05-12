import sys
sys.path.append('.')

from tkinter import Tk, Label, Button
# from field_of_game.create_sea_battle_field import matrix
from place_battle_ships_on_the_field.place_first_place_ship import matrix
# from place_battle_ships_on_the_field.place_second_place_ship import matrix
# from place_battle_ships_on_the_field.place_third_place_ship import matrix
# from place_battle_ships_on_the_field.place_fourth_place_ship import matrix
window = Tk()
window.geometry("780x730+250+100")
window.resizable(False, False)


def color(i, j):
    global matrix
    btnij.destroy()
    print('matrix', matrix[i][j], i, j)
    if str(matrix[i][j]) in ['', '0']:
        lbl = Label(window, text='', font='Arial 14 bold', fg='blue', width=5, height=2)
    else:
        lbl = Label(window, text='X', font='Arial 14 bold', fg='red', width=5, height=2)
    # lbl.grid(row=i, column=j)

for i in range(12):
    for j in range(12):
        if matrix[i][j] == '':
            matrix[i][j] = 0

for i in range(12):
    for j in range(12):
        btnij = Button(window, text=matrix[i][j], width=5, height=2, font='Arial 14', bg='green', activebackground='blue', activeforeground='white')
        btnij.grid(row=i, column=j)


window.mainloop()
#, command=lambda r=i, c=j: color(r, c)