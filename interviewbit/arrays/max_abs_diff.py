def maxArr(A):
    # max and min variables as described
    # in algorithm.
    max1 = -2147483648
    min1 = +2147483647
    max2 = -2147483648
    min2 = +2147483647
  
    for i in range(len(A)):
 
  
        # Updating max and min variables
        # as described in algorithm.
        max1 = max(max1, A[i] + i)
        min1 = min(min1, A[i] + i)
        max2 = max(max2, A[i] - i)
        min2 = min(min2, A[i] - i)
     
  
    # Calculating maximum absolute difference.
    return max(max1 - min1, max2 - min2)

A = [ -70, -64, -6, -56, 64,
           61, -57, 16, 48, -98 ]
print(maxArr(A))