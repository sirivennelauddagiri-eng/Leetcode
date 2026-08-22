class Solution(object):
    def checkDivisibility(self, n):
        temp = n
        add = 0
        product = 1
        d=0
        while n != 0:
            d = n %10
            add += d
            product *= d
            n = n//10
        return temp % (add + product) == 0


        