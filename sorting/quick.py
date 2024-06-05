def partition(arr, low, high):
    i = low
    p = low
    while (i < high):
        if (arr[i] <= arr[high]):
            arr[i], arr[p] = arr[p], arr[i]
            p+=1
        i+=1
    arr[p], arr[high] = arr[high], arr[p]
    return p
def quick_sort(arr, low, high):
    if (low < high):
        p_index = partition(arr, low, high)

        quick_sort(arr, low, p_index-1)
        quick_sort(arr, p_index+1, high)

    return arr

print(quick_sort([9, 8, 7, 6, 5, 4], 0, 5))