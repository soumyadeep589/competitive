"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    """
    with library (not good for interview)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1
    

class Solution2:
    """Sliding window technique"""
    def index_of_first_occurrence(self, needle: str, haystack: str) -> int:
        h = len(haystack)
        n = len(needle)

        if n > 0:
            for i in range(h-n+1):
                if haystack[i:i+n] == needle:
                    return i

        return -1
    
class Solution3:
    """
    KMP algorithm
    """

    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)

        # Preprocessing
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre-1]
            if needle[pre] == needle[i]:
                pre += 1
                lps[i] = pre

        # Main algorithm
        n = 0 #needle index
        for h in range(len(haystack)):
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n-1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return -1