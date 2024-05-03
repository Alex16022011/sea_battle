matrix = []
for i in range(12):
    help = []
    for j in range(12):
        help.append('')
    matrix.append(help)
for i in range(12):
    matrix[0][i] = 0
    matrix[-1][i] = 0
    matrix[i][0] = 0
    matrix[i][-1] = 0

if __name__ == '__main__':
    print(*matrix, sep="\n")
