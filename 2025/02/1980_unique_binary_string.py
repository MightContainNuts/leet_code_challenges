from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        n_length = len(nums[0])
        format_length = f'0{n_length}b'
        for i in range(2**n_length):
            if format(i, format_length) not in nums:
                return format(i, format_length)















if __name__ == '__main__':
    s = Solution()
    test1 = ["0"]

    answer = s.findDifferentBinaryString(test1)
    print(answer)
