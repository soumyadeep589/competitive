def solve(A, B):
    cnt = [0 for i in range(A)]
    s = 0
 
    # Calculating the sum of the array
    # and storing it in variable s
    s = sum(B)
 
    # Checking s is divisible by 3 or not
    if (s % 3 != 0):
        return 0
 
    # Calculating the sum of each part
    s //= 3
 
    ss = 0
 
    # If the sum of elements from i-th
    # to n-th equals to sum of part
    # putting 1 in cnt array otherwise 0.
    for i in range(A - 1, -1, -1):
 
        ss += B[i]
        if (ss == s):
            cnt[i] = 1
 
    # Calculating the cumulative sum
    # of the array cnt from the last index.
    for i in range(A - 2, -1, -1):
        cnt[i] += cnt[i + 1]
 
    ans = 0
    ss = 0
 
    # Calculating answer using original
    # and cnt array.
    for i in range(0, A - 2):
        ss += B[i]
        if (ss == s):
            ans += cnt[i + 2]
 
    return ans