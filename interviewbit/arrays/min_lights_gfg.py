""""
ref: https://www.geeksforgeeks.org/minimum-amount-of-lamps-needed-to-be-installed/
"""

import math

def min_lights(s):
    n = len(s)
    v = [""] * n
    for i in range(n):
        if s[i] == '*':
            v[i] = "*"
        
            if ( i > 0 and i < n-1):
                v[i-1] = "*"
                v[i+1] = "*"
            if (i == 0 and n != 1):
                v[i+1] = "*"
            if (i == n-1 and n != 1):
                v[i-1] = "*"

        else:
            if v[i] != "*":
                v[i] = "."

    xx = ''.join(v)

    x = xx.split("*")
    s = 0

    for i in range(len(x)):

        if x[i] == '':
            continue

        s += math.ceil(len(x[i]) / 3)
    
    return s

print(min_lights('......'))