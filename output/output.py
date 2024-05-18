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


def color(btnij, i, j):
    global matrix
    btnij.config(text='', state='disabled')
    if matrix[i][j] == 1:
        btnij.config(bg='red')
    else:
        btnij.config(bg='blue')


for i in range(12):
    for j in range(12):
        if str(matrix[i][j]) in ['', '0']:
            matrix[i][j] = 0

for i in range(12):
    for j in range(12):
        if str(matrix[i][j]) not in ['0', '']:
            matrix[i][j] = 1

for i in range(12):
    for j in range(12):
        exec(f'btn{i}_{j} = Button(window, text=matrix[{i}][{j}], width=5, height=2, font="Arial 14", bg="green", activebackground="blue", activeforeground="white", command=lambda: color(btn{i}_{j}, {i}, {j}))')
        exec(f'btn{i}_{j}.grid(row={i}, column={j})')

window.mainloop()
