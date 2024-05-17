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
    # play(matrix)
    return 'stopper'        
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