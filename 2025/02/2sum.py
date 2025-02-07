#https://leetcode.com/problems/two-sum/description/

from typing import List


test_nums = [3,3]
target = 6
answer = [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for idx,num in enumerate(nums):
            if (target-num) in num_dict:
                return [num_dict[target-num], idx]
            num_dict[num] = idx





if __name__ == '__main__':
    s = Solution()
    ans = s.twoSum(test_nums, target)
    print(ans)
    assert ans == answer


