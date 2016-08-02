def is_rearrangement_possible(matrix):
    rearrangeable = True
    matrix_size = len(matrix)
    row_index = column_index = 0
    while row_index < matrix_size and rearrangeable:
        column_index = 0
        while column_index < matrix_size and rearrangeable:
            if (column_index < matrix_size - 1 
                and matrix[row_index][column_index] > matrix[row_index][column_index + 1]):
                rearrangeable = False
            elif (row_index < matrix_size - 1 
                and matrix[row_index][column_index] > matrix[row_index + 1][column_index]):
                rearrangeable = False
            column_index += 1
            
        row_index += 1
    print "YES" if rearrangeable else "NO"

def read_and_sort_matrix_by_row():
    matrix_size = int(raw_input().strip())
    matrix = []
    for row_index in range(matrix_size):
        row = list(raw_input().strip())
        row.sort()
        matrix.append(row)
    return matrix

test_cases = int(raw_input().strip())
processed_cases = 0

while processed_cases < test_cases:
    is_rearrangement_possible(read_and_sort_matrix_by_row())
    processed_cases += 1
