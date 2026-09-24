class Solution(object):
    def smallestIndex(self, nums):
       
        for i in range(len(nums)):
            n = nums[i]
            d = 0
            while n > 0:
                d += n%10
                n = n//10
            if d == i:
                return i
        return -1
            