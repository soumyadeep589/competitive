""""
All Factors
Programming
Math
Easy
24.4% Success

107

24

Bookmark
Asked In:
Problem Description
 
 

Given a number A, find all factors of A.


Problem Constraints
1 <= A <= 109


Input Format
The first argument is an integer A.


Output Format
Return an array of all factors of A.


Example Input
A = 6


Example Output
[1, 2, 3, 6]


Example Explanation
For the given A = 6, its factors are 1, 2, 3, and 6, hence returning an array of them.
"""

import math

class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        # List to store factors, starting with 1 (since 1 is a factor of all integers)
        factors = []
        
        # Edge case for A = 1
        if A == 1:
            return [1]
        
        # Iterate from 1 to the square root of A
        for i in range(1, int(math.sqrt(A)) + 1):
            if A % i == 0:
                # i is a factor
                factors.append(i)
                # A // i is also a factor if it's different from i
                if i != A // i:
                    factors.append(A // i)
        
        # Sort the factors in ascending order
        factors.sort()
        return factors

# Example usage:
solution = Solution()
print(solution.allFactors(28))  # Output: [1, 2, 4, 7, 14, 28]