def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    out = []
    for elem in nums1:
        for i in range(0, len(nums2)):
            if elem == nums2[i]:
                nums2.pop(i)
                out.append(elem)
                break
                
    return out