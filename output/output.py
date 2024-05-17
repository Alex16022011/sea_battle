import sys
sys.path.append('.')
from tkinter import Tk, Button
from field_of_game.create_sea_battle_field import matrix
window = Tk()
window.geometry("780x730+250+100")
window.resizable(False, False)


for i in range(12):
    for j in range(12):
        exec(f"btn{i}{j} = Button(window, text=matrix[{i}][{j}], width=5, height=2, font='Arial 14', bg='green',activebackground='blue', activeforeground='white')\n"
f"btn{i}{j}.grid(row={i}, column={j})")

window.mainloop()