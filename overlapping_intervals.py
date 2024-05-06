# [15:16] Tanya Thakur
# 1.  Given a list of time intervals (start, end) Group the overlapping intervals and return an array of arrays.

# Example 1

# Input: [(1, 3), (2, 5), (8, 10), (9, 11), (15, 21)]

# Output: [[(1,5)],[(8,11)],[(15, 21)]]


# def merge_intervals(intervals):

#     intervals.sort(key = lambda x: x[0])

#     merged = []
#     group = [intervals[0]] # [(1, 3)]

#     for interval in intervals[1:]:
#         if group[0][1] >= interval[0]:
#             # group[0][1] = interval[0] # [(1, 5)]
#             group = [(group[0][0], interval[1])]
#         else:
#             merged.append(group)
#             group = [interval]
    
#     merged.append(group)

#     return merged


# print(merge_intervals([(1, 3), (2, 5), (3, 7), (8, 10), (9, 11), (15, 21)]))

