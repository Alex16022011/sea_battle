import sys
sys.path.append('.')
from tkinter import Label


# def back_index(a, found):
#     a1 = a.copy()
#     for i in range(len(a1)):
#         a1[i] = str(a1[i])
#         if a1[i] == '':
#             a1[i] = '2'
#     a1 = ''.join(a1)
#     found = str(found)
#     to_output = ''
#     if found in a1:
#         to_output = a1.rindex(found)
#     return to_output
#
#
# def start_index(a, found):
#     a1 = a.copy()
#     for i in range(len(a1)):
#         a1[i] = str(a1[i])
#         if a1[i] == '':
#             a1[i] = '2'
#     a1 = ''.join(a1)
#     found = str(found)
#     to_output = ''
#     if found in a1:
#         to_output = a1.index(found)
#     return to_output


def into_it(matrix1, ind, what_found):
    list1 = matrix1[ind].copy()
    list2 = []
    list3 = []
    for j in range(len(list1)):
        if matrix1[ind][j] == what_found:
            a = ind - 1
            if -1 < a < 11:
                if matrix1[a][j] != what_found:
                    b = ind + 1
                    if -1 < b < 11:
                        if matrix1[b][j] != what_found:
                            list3.append(matrix1[ind][j])
                            matrix1[ind][j] = ''
        else:
            list2.append(list3)
            list3 = []
    list3 = []
    for i in range(len(list2)):
        if list2[i] != []:
            list3.append(list2[i])
    return list3


def right_place_of_ship(matrix2):
    matrix1 = [e.copy() for e in matrix2]
    fourth_ship = 1
    third_ship = 2
    second_ship = 3
    first_ship = 4
    need_counter = 0
    for i in range(12):
        if matrix1[i].count(1) > 0:
            a = into_it(matrix1, i, 1)
            for j in a:
                if len(j) == 4 and fourth_ship != 0:
                    fourth_ship -= 1
                    need_counter += 1
                elif len(j) == 3 and third_ship != 0:
                    third_ship -= 1
                    need_counter += 1
                elif len(j) == 2 and second_ship != 0:
                    second_ship -= 1
                    need_counter += 1
                elif len(j) == 1 and first_ship != 0:
                    first_ship -= 1
                    need_counter += 1
                else:
                    return False

    matrix3 = []
    for i in range(11, -1, -1):
        list1 = []
        for j in range(12):
            list1.append(matrix1[j][i])
        matrix3.append(list1)
    matrix1 = matrix3.copy()

    for i in range(12):
        if matrix1[i].count(1) > 0:
            a = into_it(matrix1, i, 1)
            for j in a:
                if len(j) == 4 and fourth_ship != 0:
                    fourth_ship -= 1
                    need_counter += 1
                elif len(j) == 3 and third_ship != 0:
                    third_ship -= 1
                    need_counter += 1
                elif len(j) == 2 and second_ship != 0:
                    second_ship -= 1
                    need_counter += 1
                elif len(j) == 1 and first_ship != 0:
                    first_ship -= 1
                    need_counter += 1
                else:
                    return False
    print(f'need_counter = {need_counter}')
    if need_counter == 10:
        return True
    return False


if __name__ == '__main__':
    matrix = [['', '', '', '', '', '', '', '', '', '', '', ''],
              ['',  1,  1,  1,  1, '',  1,  1,  1, '',  1, ''],
              ['', '', '', '', '', '', '', '', '', '',  1, ''],
              ['', '', '', '', '', '', '', '', '', '',  1, ''],
              ['', '', '', '', '', '', '', '', '', '', '', ''],
              ['', '', '', '', '', '', '', '', '', '', '', ''],
              ['', '', '', '', '', '', '', '', '', '', '', ''],
              ['', '', '', '', '', '', '', '', '', '', '', ''],
              ['', '', '', '', '', '', '', '', '', '', '', ''],
              ['', '', '', '', '', '', '', '', '', '', '', ''],
              ['', '', '', '', '', '', '', '', '', '', '', ''],
              ['', '', '', '', '', '', '', '', '', '', '', '']]
    print(right_place_of_ship(matrix))
