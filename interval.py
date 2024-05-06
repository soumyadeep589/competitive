def grp_interval(arr):
    temp = 0
    out = []
    for i in range(0, len(arr)):
        x, y = arr[i]
        if i == 0:
            temp = y
            grp = [arr[i]]
        else:
            if x <= temp:
                grp.append(arr[i])
            else:
                out.append(grp)
                grp = [arr[i]]

    return out

print(grp_interval([(1, 3), (2, 5), (3,4), (8, 10), (9, 11), (15, 21)]))