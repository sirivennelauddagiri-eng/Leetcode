class Solution(object):
    def containsDuplicate(self, nums):
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                return True
            mp[nums[i]]=i
        return False
            
        
        