"""
Pick from both sides!
Programming
Arrays
Very Easy
51.1% Success

794

144

Bookmark
Asked In:
Problem Description
 
 

Given an integer array A of size N.

You have to pick exactly B elements from either left or right end of the array A to get the maximum sum.

Find and return this maximum possible sum.

NOTE: Suppose B = 4 and array A contains 10 elements then

You can pick the first four elements or can pick the last four elements or can pick 1 from the front and 3 from the back etc. you need to return the maximum possible sum of elements you can pick.


Problem Constraints
1 <= N <= 105

1 <= B <= N

-103 <= A[i] <= 103



Input Format
First argument is an integer array A.

Second argument is an integer B.



Output Format
Return an integer denoting the maximum possible sum of elements you picked.



Example Input
Input 1:

 A = [5, -2, 3 , 1, 2]
 B = 3
Input 2:

 A = [1, 2]
 B = 1


Example Output
Output 1:

 8
Output 2:

 2


Example Explanation
Explanation 1:

 Pick element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
Explanation 2:

 Pick element 2 from end as this is the maximum we can get


"""
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if B == 0:
            return 0

        head = B
        tail = len(A)
 # Initialize maximum sum as the sum of first B elements
        maxi = sum(A[:head])
        summ = maxi

# Sliding window approach
        while head > 0:
            head -= 1
            tail -= 1
    # Instead of recalculating the sum, adjust the sum by removing the head element and adding the tail element
            summ = summ - A[head] + A[tail]
            if summ > maxi:
                maxi = summ

        return maxi
    

sol = Solution()
print(sol.solve([5, -2, 3 , 1, 2], 3))