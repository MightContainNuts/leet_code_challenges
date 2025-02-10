# https://leetcode.com/problems/longest-common-prefix/description/

# GIVEN an array of strings
# WHEN they have a common prefix
# THEN return the longest common prefix from all the strings in the array

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix







if __name__ == '__main__':

    strs2 = ["ab", "a"]
    s = Solution()

    answer2 = s.longestCommonPrefix(strs2)
    print(answer2)
