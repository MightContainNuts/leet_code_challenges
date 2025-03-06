from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        """
        2d grid of size 2*2
        a appears twice and b is missing

        find a & b

        """
        n = len(grid)
        n_range = n * n
        expected_sum = n_range * (n_range+1)// 2
        expected_square_sum = n_range * (n_range + 1) * (2 * n_range + 1) // 6
        actual_sum = 0
        actual_square_sum = 0
        flat_grid = [grid[i][j] for i in range(n) for j in range(n)]

        for value in flat_grid:
            actual_sum += value
            actual_square_sum += value ** 2
        sum_difference = expected_sum - actual_sum
        square_difference =  expected_square_sum - actual_square_sum
        #a = missing number
        #b = repeated number
        a = (square_difference - sum_difference**2)//(2*sum_difference)
        #sum_difference = a - b
        b = a + sum_difference
        return [a, b]







if __name__ == '__main__':
    s = Solution()
    print(f'{s.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])} : [9,5]')
