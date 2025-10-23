def rowWithMax1s(mat):
    R = len(mat) # this one gets the number of rows
    C = len(mat[0]) # this one gets the number of columns on a row, bcs python checks the length of mat[0], hence len(mat[0])
    max1_row = -1
    row = 0
    col = C - 1

    while row < R and col >= 0:
        # this checks starting with the last column it has processed, so it will only see if there is any one other rows 
        # that have more 1s than the current row 
        if mat[row][col] == 0:
            row += 1
        else:
            max1_row = row
            col -= 1

    return max1_row


# main
mat = [[0, 0, 0, 0],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 1, 1, 1]]
print("Index of row with maximum 1s is", rowWithMax1s(mat))