"""
Max Non Negative SubArray
Programming
Arrays
Easy
14.9% Success

194

94

Bookmark
Asked In:
Problem Description

Given an array of integers, A of length N, find out the maximum sum sub-array of non negative numbers from A.

The sub-array should be contiguous i.e., a sub-array created by choosing the second and fourth element and skipping the third element is invalid.

Maximum sub-array is defined in terms of the sum of the elements in the sub-array.

Find and return the required subarray.

NOTE:  

If there is a tie, then compare with segment's length and return segment which has maximum length.
If there is still a tie, then return the segment with minimum starting index.


Problem Constraints
1 <= N <= 105

-109 <= A[i] <= 109



Input Format
The first and the only argument of input contains an integer array A, of length N.



Output Format
Return an array of integers, that is a subarray of A that satisfies the given conditions.



Example Input
Input 1:

 A = [1, 2, 5, -7, 2, 3]
Input 2:

 A = [10, -1, 2, 3, -4, 100]


Example Output
Output 1:

 [1, 2, 5]
Output 2:

 [100]


Example Explanation
Explanation 1:

 The two sub-arrays are [1, 2, 5] [2, 3].
 The answer is [1, 2, 5] as its sum is larger than [2, 3].
Explanation 2:

 The three sub-arrays are [10], [2, 3], [100].
 The answer is [100] as its sum is larger than the other two.
"""


import copy


def maxset(A):
    arr_len = len(A)
    lc_sum = 0
    max_sum = 0
    out = []
    res = []
    for i in range(0, arr_len):
        if A[i] < 0:
            out = []
            lc_sum = 0
        else:
            lc_sum += A[i]
            out.append(A[i])
            if lc_sum > max_sum:
                max_sum = lc_sum
                res = copy.deepcopy(out)
                print("print", res)
            elif lc_sum == max_sum and max_sum != 0:
                if len(res) > len(out):
                    res = copy.deepcopy(out)
            elif lc_sum == max_sum and max_sum == 0 and len(out)> len(res):
                res = copy.deepcopy(out)
    return res

# print(maxset([ 0, 0, -1, 0 ]))
print(maxset([1, 2, 5, -7, 2, 3]))