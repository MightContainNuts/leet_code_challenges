from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = 0
        min_sum = 0
        acc_sum = 0
        acc_sum_inv =0

        for num in nums:
            acc_sum += num
            acc_sum_inv += -num
            max_sum = max(max_sum, acc_sum, acc_sum_inv)
            if acc_sum < 0:
                acc_sum = 0
            if acc_sum_inv < 0:
                acc_sum_inv = 0

        return max_sum





if __name__ == '__main__':
    s = Solution()
    print(f'{s.maxAbsoluteSum([1, -3, 2, 3, -4])} (expected 5)')
    print(f'{s.maxAbsoluteSum([2,-5,1,-4,3,-2])} (expected 8)')
