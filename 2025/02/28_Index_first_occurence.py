


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)


string ="sadbutsad"

target ="sad"

if __name__ == '__main__':
    s = Solution()
    print(s.strStr(haystack=string, needle=target))
