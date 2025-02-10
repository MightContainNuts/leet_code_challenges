class Solution:
    def clearDigits(self, s: str) -> str:

        stack:str = ""

        for char in s:
            stack = stack[:-1] if char.isdigit() else stack + char
        return stack


if __name__ == '__main__':
    s = Solution()
    print(s.clearDigits("cb34"))
    print(s.clearDigits("abc"))
