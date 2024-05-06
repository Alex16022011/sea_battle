# Все в порядке до...
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

def stopper(matrix):
    global fourth_ship
    global third_ship
    global second_ship
    global first_ship
    global row_names
    global column_names
# ...сюда
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
            if len(row[i]) == 4:
                if right_order(row[i], 4):
                    matrix[i][min(row[i]) - 1] = 0
                    matrix[i][max(row[i]) + 1] = 0
                    fourth_ship -= 1
        for i in range(len(col)):
            if len(col[i]) == 4:
                if right_order(col[i], 4):
                    matrix[min(col[i]) - 1][i] = 0
                    matrix[max(col[i]) + 1][i] = 0
                    fourth_ship -= 1
        return matrix
    elif fourth_ship == 0:
        print(third_ship)
        flag = False
        if third_ship != 0:
            for i in range(12):
                if len(row[i]) == 3 or len(col[i]) == 3:
                    flag = True
        print(flag)
        if third_ship != 0 and flag:
            for i in range(len(row)):
                if len(row[i]) == 3:
                    if right_order(row[i], 3):
                        matrix[i][min(row[i]) - 1] = 0
                        matrix[i][max(row[i]) + 1] = 0
                        # third_ship -= 1
            for i in range(len(col)):
                if len(col[i]) == 3:
                    if right_order(col[i], 3):
                        matrix[min(col[i]) - 1][i] = 0
                        matrix[max(col[i]) + 1][i] = 0
            third_ship -= 1
            print(third_ship)
            return matrix
    return matrix
fourth_ship = 1
third_ship = 2
second_ship = 3 
first_ship = 4
row_names = {}
column_names = {}


if __name__ == '__main__':
    matrix = [['' for j in range(12)] for i in range(12)]
    print(matrix)
    matrix[2][2] = 1
    matrix[2][3] = 1
    matrix[2][4] = 1
    matrix[2][5] = 1
    # matrix[2][2] = 1
    # matrix[3][2] = 1
    # matrix[4][2] = 1
    # matrix[5][2] = 1
    # print(*max_limit('btn22', matrix, 2, [2, 3, 4, 5]), sep='\n')
    print(*stopper(matrix), sep='\n')