#3066. Minimum Operations to Exceed Threshold Value II
import heapq
from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        operations = 0

        heapq.heapify(nums)
        while nums[0]<k:
            operations += 1
            num_1, num_2 = heapq.heappop(nums), heapq.heappop(nums)
            new_number = num_1*2 + num_2
            heapq.heappush(nums,new_number)
        return operations






if __name__ == '__main__':
    s = Solution()
    test_case_1 = [2,11,10,1,3]
    k_1 = 10
    expected_ans_1 = 2
    test_case_2 = [999999999,999999999,999999999]
    k_2 = 1000000000
    expected_ans_2 = 2


    # ans_1 = s.minOperations(test_case_1, k_1)
    # print( ans_1, expected_ans_1)

    ans_2 = s.minOperations(test_case_2, k_2)
    print(ans_2, expected_ans_2)
