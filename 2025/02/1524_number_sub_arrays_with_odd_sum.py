from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:

        even, odd, result = 0,0,0

        for num in arr:
            if num % 2 == 0: even = even + 1
            else: even, odd  = odd, even +1
            result += odd

        return result % (10 ** 9 +7)












if __name__ == '__main__':
    s = Solution()
    ans_1 = s.numOfSubarrays([1,2,3,4,5,6,7])
    print(ans_1)
    assert ans_1 == 16
