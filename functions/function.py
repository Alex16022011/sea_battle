import sys
sys.path.append('.')
def right_order(obj, len):
    counter = 0
    counter2 = 0
    for i in range(len - 1, 0, -1):
        if obj[i] - obj[i - 1] == 1:
            counter += 1
        else:
            return False
        counter2 += 1
    if counter == counter2:
        return True

# def checker(matrix, dct, col_or_row):
#     if col_or_row == 0:
#         # row
#         for i in dct.keys():
#             if i == 'fourth':
#                 t = dct[i]
#                 for j in t.keys():
#                     a, b = t[j]
#                     if abs(b) - abs(a) != 5:
#                         return None
#                     counter = 0
#                     counter2 = 0
#                     for k in range(a + 1, b):
#                         if str(matrix[j][k]) not in '0""':
#                             counter += 1
#                         counter2 += 1
#                     if counter != counter2:
#                         matrix[j][a] = ''
#                         matrix[j][b] = ''
#     else:
#         # col
#         for i in dct.keys():
#             if i == 'fourth':
#                 t = dct[i]
#                 for j in t.keys():
#                     a, b = t[j]
#                     if abs(b) - abs(a) != 5:
#                         return None
#                     counter = 0
#                     counter2 = 0
#                     for k in range(a + 1, b):
#                         if str(matrix[k][j]) not in '0""':
#                             counter += 1
#                         counter2 += 1
#                     if counter != counter2:
#                         matrix[a][j] = ''
#                         matrix[b][j] = ''
#     return matrix

def right_place_of_ship(matrix, dct1, dct2):
    global fourth_ship
    global third_ship
    global second_ship
    global first_ship
    for i in range(len(matrix)):
        counter = 0
        counter2 = 0
        if matrix[i].count(1) > 0:
            for j in range(len(matrix[0])):
                if  matrix[i][j] == 1:
                    counter += 1
                counter2 += 1
                if matrix[i][j] != 1:
                    break
            if counter == counter2:
                if counter == 4:
                    if fourth_ship != 0:
                        fourth_ship -= 1
                    else:
                        return False
                elif counter == 3:
                    pass
                elif counter == 2:
                    pass
                elif counter == 1:
                    pass


def stopper(matrix):
    global fourth_ship
    global third_ship
    global second_ship
    global first_ship
    global row_names
    global column_names
    global stopper_points_row
    global stopper_points_column
    global row_ship
    global column_ship
    row = {}
    col = {}
    flag = False
    for i in range(12):
        row[i] = []
        col[i] = []
        for j in range(12):
            if str(matrix[i][j]) not in "''0":
                row[i].append(j)
            if str(matrix[j][i]) not in "''0":
                col[i].append(j)
    if fourth_ship != 0:
        for i in range(12):
            if len(row[i]) == 4 or len(col[i]) == 4:
                flag = True

    if fourth_ship != 0 and flag:
        for i in range(len(row)):
            stopper_points_row[i] = []
            if len(row[i]) == 4:
                if right_order(row[i], 4):
                    matrix[i][min(row[i]) - 1] = 0
                    matrix[i][max(row[i]) + 1] = 0
                    stopper_points_row[i].append((min(row[i]) - 1, max(row[i]) + 1))
                    fourth_ship -= 1
                    row_ship['fourth'] = {i: (min(row[i]) - 1, max(row[i]) + 1)}
        for i in range(len(col)):
            stopper_points_column[i] = []
            if len(col[i]) == 4:
                if right_order(col[i], 4):
                    matrix[min(col[i]) - 1][i] = 0
                    matrix[max(col[i]) + 1][i] = 0
                    stopper_points_column[i].append((min(col[i]) - 1, max(col[i]) + 1))
                    fourth_ship -= 1
                    column_ship['fourth'] = {i: (min(col[i]) - 1, max(col[i]) + 1)}
    # for i in row_ship.keys():
    #     if i == 'fourth':
    #         matrix = checker(matrix, row_ship, 0)
    #         fourth_ship += 1
    #     elif i == 'third':
    #         pass
    #     elif i == 'second':
    #         pass
    #     elif i == 'first':
    #         pass
    
    # for i in column_ship.keys():
    #     if i == 'fourth':
    #         matrix = checker(matrix, column_ship, 1)
    #         fourth_ship += 1
    #     elif i == 'third':
    #         pass
    #     elif i == 'second':
    #         pass
    #     elif i == 'first':
    #         pass

        # print(stopper_points_row)
        # print(stopper_points_column)
        # for i in stopper_points_row.keys():
        #     if stopper_points_row[i] != ():
        #         counter = 0
        #         for j in range(stopper_points_row[i][0] + 1, stopper_points_row[i][1]):
        #             if matrix[i][j] not in '0""':
        #                 counter += 1
        #     if counter != 4:
        #         matrix[i][stopper_points_row[i][0]] = ''
        #         matrix[i][stopper_points_row[i][1]] = ''

    # elif fourth_ship == 0:
    #     print(third_ship)
    #     flag = False
    #     if third_ship != 0:
    #         for i in range(12):
    #             if len(row[i]) == 3 or len(col[i]) == 3:
    #                 flag = True
    #     print(flag)
    #     if third_ship != 0 and flag:
    #         for i in range(len(row)):
    #             if len(row[i]) == 3:
    #                 if right_order(row[i], 3):
    #                     matrix[i][min(row[i]) - 1] = 0
    #                     matrix[i][max(row[i]) + 1] = 0
    #                     # third_ship -= 1
    #         for i in range(len(col)):
    #             if len(col[i]) == 3:
    #                 if right_order(col[i], 3):
    #                     matrix[min(col[i]) - 1][i] = 0
    #                     matrix[max(col[i]) + 1][i] = 0
    #         third_ship -= 1
    #         print(third_ship)
    #         return matrix
    return matrix
fourth_ship = 1
third_ship = 2
second_ship = 3 
first_ship = 4
row_names = {}
column_names = {}
stopper_points_row = {}
stopper_points_column = {}
row_ship = {}
column_ship = {}

if __name__ == '__main__':
    matrix = [['' for j in range(12)] for i in range(12)]
    print(matrix)
    matrix[2][1] = 0
    matrix[2][2] = 1
    matrix[2][3] = 1
    # matrix[2][4] = 1
    matrix[2][5] = 1
    matrix[2][6] = 0
    # matrix[2][2] = 1
    # matrix[3][2] = 1
    # matrix[4][2] = 1
    # matrix[5][2] = 1
    # print(*max_limit('btn22', matrix, 2, [2, 3, 4, 5]), sep='\n')
    print(*stopper(matrix), sep='\n')