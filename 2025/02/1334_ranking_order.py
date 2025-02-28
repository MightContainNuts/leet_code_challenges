from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        dict_rank = {val: rank + 1 for rank, val in
                     enumerate(sorted_arr)}
        return [dict_rank[val] for val in arr]




if __name__ == '__main__':
    s = Solution()
    print(s.arrayRankTransform([40,10,20,30]))
