from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        search_index = 1
        for element in nums[1:]:
            if element != nums[search_index - 1]:
                nums[search_index] = element
                search_index += 1
        return search_index




if __name__ == '__main__':
    s = Solution()
    print(f"Answer = {s.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])}")
