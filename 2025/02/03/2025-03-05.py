class Solution:
    def coloredCells(self, n: int) -> int:
        EXPANSION_RATIO = 4

        return 1 + (n * (n - 1) * EXPANSION_RATIO // 2)
