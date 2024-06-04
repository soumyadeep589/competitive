def insertion_sort(arr):

    for i in range(1, len(arr)):
        key = arr[i] 
        j = i-1      
        while(j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key

    return arr


print(insertion_sort([9, 8, 7, 6, 5, 4, 3]))

