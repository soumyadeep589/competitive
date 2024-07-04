""""
Add One To Number
Programming
Arrays
Easy
19.3% Success

440

68

Bookmark
Asked In:
Problem Description
 
 

Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.

NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example: 
for this problem, following are some good questions to ask :

Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.


Problem Constraints
1 <= |A| <= 106
0 <= Ai <= 9


Input Format
First argument is an array of digits.



Output Format
Return the array of digits after adding one.



Example Input
Input 1:

[1, 2, 3]


Example Output
Output 1:

[1, 2, 4]


Example Explanation
Explanation 1:

Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
"""



def plusOne(A):
    arr = A[::-1]
    
    arr[0] = arr[0] + 1
    i = 0
    while(True):
        if arr[i] == 10:
            arr[i] = 0
            if i != len(A) - 1:
                arr[i+1] = arr[i+1] + 1
            else:
                arr.append(1)
                break
            i += 1
        else:
            break
    while (True):
        if arr[len(arr)-1] == 0:
            arr.pop()
        else: break
    res = arr[::-1]

    return res

print(plusOne([0, 3, 9, 9]))