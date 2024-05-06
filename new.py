# Given a list of time intervals (start, end) Group the overlapping intervals and return an array of arrays. Hint: Let's assume the intervals are sorted by the interval start time.

# Example 1

# Input: [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]

# Output: [[(1, 3), (2, 5)], [(8, 10), (9, 11)], [(15, 21)]]


# Example 2

# Input: [(1, 3), (2, 5), (3,4), (8, 10), (9, 11), (15, 21)]

# Output:[[(1, 3), (2, 5), (3, 4)], [(8, 10), (9, 11)], [(15, 21)]]




def grp_interval(arr):
    temp = 0
    out = []
    grp = []
    for i in range(0, len(arr)):
        x, y = arr[i]
        if (i == 0):
            temp = y
            grp = [arr[i]]
        else:
            if (x <= temp):
                grp.append(arr[i])
            else:
                out.append(grp)
                grp = [arr[i]]
                temp = y
    out.append(grp)
    return out
print(grp_interval([(1, 3), (2, 5), (3,4), (8, 10), (9, 11), (15, 21), (20, 25)]))