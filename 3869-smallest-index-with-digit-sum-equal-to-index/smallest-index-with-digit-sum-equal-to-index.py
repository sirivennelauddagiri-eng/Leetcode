class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            d = 0
            while nums[i] > 0:
                d += nums[i]%10
                nums[i] //= 10
            if d == i:
                return i
        return -1
            