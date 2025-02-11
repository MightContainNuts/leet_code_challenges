class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:


        while True:
            if part in s:
                s = s.replace(part,"",1)
            else:
                return s





if __name__ == '__main__':
    sol = Solution()
    string = "aabababa"
    substring ="aba"
    expected_result ="ba"
    answer = sol.removeOccurrences(string,substring)
    assert answer == expected_result
