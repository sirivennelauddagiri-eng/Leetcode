class Solution(object):
    def isHappy(self, n):
        s = set()
        while n != 1:
            if n in s:
                return False
            s.add(n)
            t = 0
            while n>0:
                d = n%10
                t += d*d
                n //= 10
            n = t
        return True
