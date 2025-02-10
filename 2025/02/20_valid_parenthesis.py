from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        mapped_chars = {
            ")":"(",
            "}":"{",
            "]":"["
         }

        stack:List = []

        if not s or s[0] in mapped_chars:
            return False

        for char in s:
            if char and stack and mapped_chars.get(char) == stack[-1]:
                stack.pop()

            else:
                stack.append(char)
        return True if not stack else False



if __name__ == '__main__':
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([])"
    ]
    s= Solution()
    print(s.isValid("([])"))

