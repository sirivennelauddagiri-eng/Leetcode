class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        if num == 0:
            return 0
        if num % 2 == 0:
            return 1+self.numberOfSteps(num//2)
        else:
            return 1+self.numberOfSteps(num-1)

        