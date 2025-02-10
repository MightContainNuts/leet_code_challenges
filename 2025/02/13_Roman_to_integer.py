# https://leetcode.com/problems/roman-to-integer/


class Solution:
    def romanToInt(self, s: str) -> int:
        """convert roman numerical string to int"""
        mapped_numerals ={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D": 500,
            "M": 1000
        }
        prev_value:int = 0
        accumulate_value:int = 0

        for char in reversed(s):
            actual_value = mapped_numerals[char]
            accumulate_value += actual_value \
                if actual_value >= prev_value \
                else -actual_value
            prev_value = actual_value
        return accumulate_value

if __name__ == '__main__':
    s = Solution()
    answer = s.romanToInt("MCMLXVIII")
    print(answer)
