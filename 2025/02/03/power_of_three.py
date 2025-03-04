class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 0:
            return False

        BASE = 3
        while n > 0:
            if n % BASE == 2:
                return False
            n //= BASE

        return True





if __name__ == '__main__':
    s = Solution()
    print(s.checkPowersOfThree(12)) # True
    print(s.checkPowersOfThree(91)) # True
    print(s.checkPowersOfThree(21)) # False
