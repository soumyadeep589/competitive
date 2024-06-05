def bubble_sort(arr):

    for i in range(len(arr)):
        swapped = False

        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            return arr
        
    return arr

print(bubble_sort([9, 8, 7, 6, 5, 4, 3]))