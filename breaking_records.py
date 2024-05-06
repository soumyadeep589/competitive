def breakingRecords(scores):
    # Write your code here
    minout = 0
    maxout = 0
    min_score = 0
    max_score = 0
    for i, e in enumerate(scores):
        if i == 0:
            min_score = e
            max_score = e
        else:
            if e > max_score:
                maxout += 1
                max_score = e
            elif e < min_score:
                minout += 1
                min_score = e
    
    return [minout, maxout]


print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))