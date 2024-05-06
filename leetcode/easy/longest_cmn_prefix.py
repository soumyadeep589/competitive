"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    letters = list(strs[0])
    i = 0
    out_str = ""
    while (i < len(strs[0])):
        for word in strs[1:]:
            if i >= len(word):
                return out_str
            if  word[i] not in letters:
                return out_str
            if letters[i] != word[i]:
                return out_str
        
        out_str += strs[0][i]
        i += 1
    return out_str

print(longestCommonPrefix(["flower","flow","flight"]))