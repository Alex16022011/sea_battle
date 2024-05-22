def create_field(row, cols):
    if row != cols:
        return None
    matrix = []
    for i in range(row):
        help = []
        for j in range(cols):
            help.append('')
        matrix.append(help)
    for i in range(row):
        matrix[0][i] = 0
        matrix[-1][i] = 0
        matrix[i][0] = 0
        matrix[i][-1] = 0
    return matrix


matrix = create_field(12, 12)

if __name__ == '__main__':
    print(*matrix, sep="\n")
