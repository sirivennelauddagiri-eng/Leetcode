class Solution(object):
    def twoSum(self, nums, target):
       mp = {}
       for i in range(len(nums)):
            c = target - nums[i]
            if c in mp:
                return [mp[c],i]
            mp[nums[i]]=i