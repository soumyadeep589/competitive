def two_sum(nums, target):
    seen = {}
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        
        if remaining in seen:
            return True
        
        seen[value] = i 

    return False


print(two_sum ([2, 7, 11, 12], 9))