# [15:16] Tanya Thakur
# 1.  Given a list of time intervals (start, end) Group the overlapping intervals and return an array of arrays.

# Example 1

# Input: [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]

# Output: [[(1,5)],[(8,11)],[(15, 21)]]

def merge_intervals(intervals):
    # Sort the intervals based on the start value
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If the merged list is empty or if the current interval does not overlap with the last interval in the merged list
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            # Merge the current interval with the last interval in the merged list
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))

    return merged

# Test the function
intervals = [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]
result = merge_intervals(intervals)
print(result)  # Output: [(1, 5), (8, 11), (15, 21)]

# Given an array of integers, write a function to find the maximum product of three numbers in the array.
# nums = [1, 2, 3, 4, 5]

def max_product(arr):
    arr.sort()
    return arr[len(arr)-1] * arr[len(arr)-2] * arr[len(arr)-3]

print(max_product([1, 2, 3, 4, 5]))