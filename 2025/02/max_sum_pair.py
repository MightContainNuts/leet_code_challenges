from typing import List
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        digit_sum_list = [sum(int(digit) for digit in str(num)) for num in nums]
        digit_num_list = zip(nums, digit_sum_list)
        sorted_list = sorted(digit_num_list, key = lambda x: (x[1], x[0]), reverse = True)

        total = -1
        stack = [-1,-1]
        for element in sorted_list:
            print(element[0], element[1])
            num, digit_sum = element[0], element[1]
            num_stack, digit_sum_stack = stack[0], stack[1]
            if digit_sum == digit_sum_stack and num + num_stack > total:
                total = num + num_stack
            stack[0], stack[1] = num, digit_sum
        return total
