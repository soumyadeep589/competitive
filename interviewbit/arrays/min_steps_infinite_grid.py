"""
**GFG**
https://www.geeksforgeeks.org/minimum-steps-needed-to-cover-a-sequence-of-points-on-an-infinite-grid/
"""

def min_step(p, q):
    return max(abs(p[0]-q[0]), abs(p[1]-q[1]))


def cover_points(seqs):
    path = 0
    size = len(seqs)
    for i in range(0, size-1):
        min_path = min_step(seqs[i], seqs[i+1])
        path = path + min_path
    return path

print(cover_points([[4, 6] ,[ 1, 2 ], [ 4, 5] , [ 10, 12]] ))


"""
**INTERVIEWBIT**
Min Steps in Infinite Grid
Programming
Arrays
Easy
44.4% Success

386

59

Bookmark
Asked In:
Problem Description
 
 

You are in an infinite 2D grid where you can move in any of the 8 directions

 (x,y) to 
    (x-1, y-1), 
    (x-1, y)  , 
    (x-1, y+1), 
    (x  , y-1),
    (x  , y+1), 
    (x+1, y-1), 
    (x+1, y)  , 
    (x+1, y+1) 
You are given a sequence of points and the order in which you need to cover the points.. Give the minimum number of steps in which you can achieve it. You start from the first point.

NOTE: This question is intentionally left slightly vague. Clarify the question by trying out a few cases in the “See Expected Output” section.



Problem Constraints
1 <= |A| <= 106
- 2 * 103 <= Ai, Bi <= 2 * 103
|A| == |B|


Input Format
Given two integer arrays A and B, where A[i] is x coordinate and B[i] is y coordinate of ith point respectively.



Output Format
Return an Integer, i.e minimum number of steps.



Example Input
Input 1:

 A = [0, 1, 1]
 B = [0, 1, 2]


Example Output
Output 1:

 2


Example Explanation
Explanation 1:

 Given three points are: (0, 0), (1, 1) and (1, 2).
 It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    
    
    def coverPoints(self, A, B):
        def min_step(p, q):
            return max(abs(p[0]-q[0]), abs(p[1]-q[1]))
        path = 0
        size = len(A)
        if size == 1:
            return 0
        for i in range(0, size-1):
            min_path = min_step([A[i], B[i]], [A[i+1], B[i+1]])
            path = path + min_path
        return path