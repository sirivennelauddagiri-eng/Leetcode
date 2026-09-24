class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            d = 0
            n = nums[i] 
            while n > 0:
                d += n%10
                n //= 10
            if d == i:
                return i
        return -1
            