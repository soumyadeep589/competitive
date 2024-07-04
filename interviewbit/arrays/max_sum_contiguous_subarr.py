""""
KADANE's ALGO
ref: https://www.youtube.com/watch?v=AHZpyENo7k4&ab_channel=takeUforward

Max Sum Contiguous Subarray
Programming
Arrays
Easy
32.6% Success

608

26

Bookmark
Asked In:
Problem Description
 
 

Find the contiguous subarray within an array, A of length N which has the largest sum.


Problem Constraints
1 <= N <= 106
-1000 <= A[i] <= 1000


Input Format
The first and the only argument contains an integer array, A.


Output Format
Return an integer representing the maximum possible sum of the contiguous subarray.


Example Input
Input 1:
A = [1, 2, 3, 4, -10]
Input 2:
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


Example Output
Output 1:
10
Output 2:
6


Example Explanation
Explanation 1:
The subarray [1, 2, 3, 4] has the maximum possible sum of 10.
Explanation 2:
The subarray [4,-1,2,1] has the maximum possible sum of 6.
"""


inf = float('inf')

class Solution:
	# @param A : tuple of integers
	# @return an integer
    def maxSubArray(self, A):
        best = -inf
        sumsofar = 0
        for x in A:
            sumsofar += x
            best = max(sumsofar, best)
            # Doing this last, to handle case
            # when all numbers are negative.
            sumsofar = max(sumsofar, 0)
        return best
