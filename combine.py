def combine(arr1, arr2):
    out = []
    if len(arr1) != len(arr2):
        return "length of two arr must be same"
    else:
        for index, value in enumerate(arr1):
            out.append(arr1[index])
            out.append(arr2[index])
        return out


print(combine(["a", "b", "c"], [1, 2, 3]))