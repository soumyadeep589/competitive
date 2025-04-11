def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while(low <= high):
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary_search([1, 3, 11, 24, 36, 47, 57, 78, 90], 90))