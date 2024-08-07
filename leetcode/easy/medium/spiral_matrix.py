"""
54. Spiral Matrix
Medium
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100


"""




class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        row_start = 0 # starting row
        row_end = len(matrix) # ending row
        col_start = 0 # staring col
        col_end = len(matrix[0]) # ending col
        while (row_start < row_end and col_start < col_end):
            for i in range(col_start, col_end):
                arr.append(matrix[row_start][i])
                
            row_start+=1
            for i in range(row_start, row_end):
                arr.append(matrix[i][col_end-1])
            col_end-=1
            if (row_start < row_end):
                for i in range(col_end-1, col_start-1, -1):
                    arr.append(matrix[row_end-1][i])
                row_end-=1
            if (col_start < col_end):
                for i in range(row_end-1, row_start-1, -1):
                    arr.append(matrix[i][col_start])
                col_start+=1
        return arr