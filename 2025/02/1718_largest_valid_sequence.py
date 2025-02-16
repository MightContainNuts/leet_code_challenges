from typing import List


class Solution:

    def __init__(self):
        self.array = []

    def constructDistancedSequence(self,n) -> List[int]:
        self.create_array(n)

    def create_array(self,n):
        self.array = [-1] *  (2 * n -1)
        print(self.array)


if __name__ == '__main__':
    s = Solution()
    num = 3
    exp_output = [3,1,2,3,2]

    result = s.constructDistancedSequence(num)
    print(result)
    assert result == exp_output
