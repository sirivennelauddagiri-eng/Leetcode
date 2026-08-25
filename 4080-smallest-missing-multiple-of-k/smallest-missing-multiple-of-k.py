class Solution(object):
    def missingMultiple(self, nums, k):
        i = 1 
        while k != 0:
            m = i*k
            if m not in nums:
                return m
            i += 1