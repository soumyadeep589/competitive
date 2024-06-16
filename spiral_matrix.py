"""
Given a matrix of M * N elements (M rows, N columns), return all elements of the matrix in spiral order.


Problem Constraints
1 <= M, N <= 1000


Input Format
The first argument is a matrix A.


Output Format
Return an array of integers representing all elements of the matrix in spiral order.


Example Input
A = 
    [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]


Example Output
[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""

# @param A : tuple of list of integers
# @return a list of integers
def spiralOrder(A):
    arr = []
    row_start = 0 # starting row
    row_end = len(A) # ending row
    col_start = 0 # staring col
    col_end = len(A[0]) # ending col
    while (row_start < row_end and col_start < col_end):
        for i in range(col_start, col_end):
            arr.append(A[row_start][i])
            
        row_start+=1
        for i in range(row_start, row_end):
            arr.append(A[i][col_end-1])
        col_end-=1
        if (row_start < row_end):
            for i in range(col_end-1, col_start-1, -1):
                arr.append(A[row_end-1][i])
            row_end-=1
        if (col_start < col_end):
            for i in range(row_end-1, row_start-1, -1):
                arr.append(A[i][col_start])
            col_start+=1
    return arr

A = [
    [1, 2, ],
]
print(spiralOrder(A))