from typing import List, Optional

class Solution:

    @staticmethod
    def closestPrimes(left: int, right: int) -> List[int]:

        list_of_primes = Solution.sieve_of_eratosthenes(left, right)

        if len(list_of_primes) < 2:
            return [-1, -1]

        num1, num2 = -1, -1
        diff = float('inf')
        for i in range(1, len(list_of_primes)):
            if list_of_primes[i] - list_of_primes[i - 1] < diff:
                diff = list_of_primes[i] - list_of_primes[i - 1]
                num1, num2 = list_of_primes[i - 1], list_of_primes[i]

        return [num1, num2]

    @staticmethod
    def sieve_of_eratosthenes(left: int, right: int) -> List[int]:

        sieve_size = right - left + 1
        primes = [True] * sieve_size


        if left == 0:
            primes[0] = False
        if left <= 1:
            primes[1 - left] = False


        for i in range(2, int(right ** 0.5) + 1):

            start = max(i * i, (left + i - 1) // i * i)
            for j in range(start, right + 1, i):
                primes[j - left] = False


        return [i for i in range(left, right + 1) if primes[i - left]]


if __name__ == '__main__':
    s = Solution()
    print(s.closestPrimes(10,20)) # [11, 13])
