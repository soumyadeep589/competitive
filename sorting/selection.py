def min_index(arr, start):

    min_index = start
    for i in range(start+1, len(arr)):
        if arr[i] < arr[min_index]:
            min_index = i
    return min_index

def selection_sort(arr):
    i = 0

    while (i<len(arr)):
        min = min_index(arr, i)

        if i != min:
            arr[i], arr[min] = arr[min], arr[i]
        
        i+=1
    return arr

print(selection_sort([9, 8, 7, 6, 5, 4, 3]))