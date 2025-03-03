from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums_lt_pivot = []
        nums_gt_pivot = []
        counter =0

        for num in nums:

            if num < pivot:
                nums_lt_pivot.append(num)
            elif num > pivot:
                nums_gt_pivot.append(num)
            else:
                counter +=1

        return nums_lt_pivot + [pivot] * counter + nums_gt_pivot






if __name__ == '__main__':
    s = Solution()
    print(s.pivotArray([9, 12, 3, 5, 14, 10, 10], 10))  # [9, 3, 5, 10, 10, 12, 14]
