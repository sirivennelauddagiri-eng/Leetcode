class Solution(object):
    def majorityElement(self, nums):
        c =  0
        for i in nums:
            if c == 0:
                el = i
                c = 1
            elif i == el:
                c += 1
            else:
                c -= 1
        c1 = 0
        for i in nums:
            if i == el:
                c1 += 1
        if c1 > len(nums)//2:
            return el

        
        