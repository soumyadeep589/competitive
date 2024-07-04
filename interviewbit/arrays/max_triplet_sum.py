""""
Maximum Sum Triplet
Programming
Arrays
Medium
33.1% Success

717

66

Bookmark
Asked In:
Problem Description
 
 

Given an array A containing N integers.

You need to find the maximum sum of triplet ( Ai + Aj + Ak ) such that 0 <= i < j < k < N and Ai < Aj < Ak.

If no such triplet exist return 0.



Problem Constraints
3 <= N <= 105.

1 <= A[i] <= 108.



Input Format
First argument is an integer array A.



Output Format
Return a single integer denoting the maximum sum of triplet as described in the question.



Example Input
Input 1:

 A = [2, 5, 3, 1, 4, 9]
Input 2:

 A = [1, 2, 3]


Example Output
Output 1:

 16
Output 2:

 6


Example Explanation
Explanation 1:

 All possible triplets are:-
    2 3 4 => sum = 9
    2 5 9 => sum = 16
    2 3 9 => sum = 14
    3 4 9 => sum = 16
    1 4 9 => sum = 14
  Maximum sum = 16
Explanation 2:

 All possible triplets are:-
    1 2 3 => sum = 6
 Maximum sum = 6
"""

import bisect
import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        # Function to get the lower last min value of 'n'
        def getLowValue(lowValue, n):
            it = bisect.bisect_left(lowValue, n)
            if it == 0:
                return -sys.maxsize
            else:
                return lowValue[it-1]

    # Initialize suffix-array
        maxSuffArr = [0] * (n + 1)

        # Set the last element
        maxSuffArr[n] = 0

        # Calculate suffix-array containing maximum
        # value for index i, i+1, i+2, ... n-1 in arr[i]
        for i in range(n-1, -1, -1):
            maxSuffArr[i] = max(maxSuffArr[i + 1], A[i])

        ans = 0

        # Initialize list to store minimum values
        lowValue = [-sys.maxsize]

        for i in range(n - 1):
            if maxSuffArr[i + 1] > A[i]:
                ans = max(ans, getLowValue(lowValue, A[i])
                        + A[i] + maxSuffArr[i + 1])

                # Insert arr[i] in list for further processing
                bisect.insort_left(lowValue, A[i])

        return ans
                