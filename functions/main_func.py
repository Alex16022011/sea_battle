import sys
sys.path.append('.')
sys.path.append('C:/Users/МойКомпьютер/.vscode/sea_battle/functions/main_functions')
from tkinter import Label
def back_index(a, found):
    for i in range(len(a)):
        a[i] = str(a[i])
    a = ''.join(a)
    found = str(found)
    to_output = ''
    if found in a:
        to_output = a.rindex(found)
    return to_output

def start_index(a, found):
    for i in range(len(a)):
        a[i] = str(a[i])
    a = ''.join(a)
    found = str(found)
    to_output = ''
    if found in a:
        to_output = a.index(found)
    return to_output

def into_it(list1):
    list2 = []
    list3 = []
    for i in range(len(list1)):
        if list1[i] == 1:
            list3.append(list1[i])
        else:
            list2.append(list3)
            list3 = []
    list3 = []
    for i in range(len(list2)):
        if list2[i] != []:
            list3.append(list2[i])
    return list3


def right_place_of_ship(matrix1):
    global fourth_ship
    global third_ship
    global second_ship
    global first_ship
    need_counter = 0
    for i in range(12):
        if matrix1[i].count(1) > 0:
            a = back_index(matrix1[i], 1) - start_index(matrix1[i], 1)  
            if -1 < a < 4:
                if a == 0 and first_ship != 0:
                    first_ship -= 1
                elif a == 1 and second_ship != 0:
                    second_ship -= 1
                elif a == 2 and third_ship != 0:
                    third_ship -= 1
                elif a == 3 and fourth_ship != 0:
                    fourth_ship -= 1
                else:
                    return False
                need_counter += 1
            else:
                a = into_it(matrix1[i])
                for j in a:
                    if len(j) == 4 and fourth_ship != 0:
                        fourth_ship -= 1
                    elif len(j) == 3 and third_ship != 0:
                        third_ship -= 1
                    elif len(j) == 2 and second_ship != 0:
                        second_ship -= 1
                    elif len(j) == 1 and first_ship != 0:
                        first_ship -= 1
                    else:
                        return False
                    need_counter += 1



    matrix3 = []
    for i in range(12):
        list1 = []
        for j in range(12):
            list1.append(matrix1[j][i])
        matrix3.append(list1)
    matrix1 = matrix3.copy()

    for i in range(12):
        if matrix1[i].count(1) > 0:
            a = back_index(matrix1[i], 1) - start_index(matrix1[i], 1)  
            if -1 < a < 4:
                if a == 0 and first_ship != 0:
                    first_ship -= 1
                elif a == 1 and second_ship != 0:
                    second_ship -= 1
                elif a == 2 and third_ship != 0:
                    third_ship -= 1
                elif a == 3 and fourth_ship != 0:
                    fourth_ship -= 1
                else:
                    return False
                need_counter += 1
            else:
                a = into_it(matrix1[i])
                for j in a:
                    if len(j) == 4 and fourth_ship != 0:
                        fourth_ship -= 1
                    elif len(j) == 3 and third_ship != 0:
                        third_ship -= 1
                    elif len(j) == 2 and second_ship != 0:
                        second_ship -= 1
                    elif len(j) == 1 and first_ship != 0:
                        first_ship -= 1
                    else:
                        return False
                    need_counter += 1
    if need_counter == 2:
        return True
    return False

def play(matrix):
    counter = 0
    lbl = Label(text='Вы неправильно расставили корабли', font='Arial 20')
    if right_place_of_ship(matrix):
        if counter == 1:
            lbl.destroy()
    else:
        lbl.grid(row=12, column=0, columnspan=11)
        counter = 1