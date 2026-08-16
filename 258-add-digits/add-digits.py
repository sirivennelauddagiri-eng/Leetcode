class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            add = 0
            while num > 0:
                d = num % 10
                add += d
                num = num // 10
            num = add
        return num


        