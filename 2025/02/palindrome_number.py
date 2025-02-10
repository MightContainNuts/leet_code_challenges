#https://leetcode.com/problems/palindrome-number/

#GIVEN an integer x
#WHEN x is a palindrome
#THEN return True
#ELSE return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        int_as_str = str(x)
        return True if int_as_str == int_as_str[::-1] else False





if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
