class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True]*n
        is_prime[0] = False
        is_prime[1] = False
        for i in range(4,n,2):
            is_prime[i] = False
        p = 3
        while p * p <n:
            if is_prime[p]:
                for i in range(p*p,n,2*p):
                    is_prime[i] = False
            p += 2
        return is_prime.count(True)
        