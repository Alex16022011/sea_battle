import sys
sys.path.append('.')
from functions.main_func import right_place_of_ship
from tkinter import Label


# def right_order(obj, length):
#     counter = 0
#     counter2 = 0
#     for i in range(length - 1, 0, -1):
#         if obj[i] - obj[i - 1] == 1:
#             counter += 1
#         else:
#             return False
#         counter2 += 1
#     if counter == counter2:
#         return True
#
#
# def right_place_of_ship(matrix):
#     global fourth_ship
#     global third_ship
#     global second_ship
#     global first_ship
#     for i in range(len(matrix)):
#         counter = 0
#         counter2 = 0
#         if matrix[i].count(1) > 0:
#             for j in range(len(matrix[0])):
#                 if matrix[i][j] == 1:
#                     counter += 1
#                 counter2 += 1
#                 if matrix[i][j] != 1:
#                     break
#             if counter == counter2:
#                 if counter == 4:
#                     if fourth_ship != 0:
#                         fourth_ship -= 1
#                     else:
#                         return False
#                 elif counter == 3:
#                     pass
#                 elif counter == 2:
#                     pass
#                 elif counter == 1:
#                     pass
#

def stopper(matrix_of_user):
    global counter
    for i in range(12):
        for j in range(12):
            if str(matrix_of_user[i][j]).isdigit() and int(matrix_of_user[i][j]) > 0:
                matrix_of_user[i][j] = int(matrix_of_user[i][j])
    lbl = Label(text='Вы неправильно расставили корабли', font='Arial 20')
    if right_place_of_ship(matrix_of_user):
        if counter == 1:
            lbl2 = Label(text='                                                           ', font='Arial 20')
            lbl2.grid(row=12, column=6, columnspan=13)
            counter = 0
            return True
    else:
        lbl.grid(row=12, column=6, columnspan=13)
        counter = 1
        return False
    print(f'counter = {counter}')


counter = 0


if __name__ == '__main__':
    matrix = [['' for j in range(12)] for i in range(12)]