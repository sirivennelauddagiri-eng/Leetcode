class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n > 0:
            half = self.myPow(x,n/2)
            if n%2 == 0:
                return half*half
            else:
                return half*half*x
        if n < 0:
            n = -n
            return 1/self.myPow(x,n)

        