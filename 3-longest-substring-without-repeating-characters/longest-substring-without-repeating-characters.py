class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        l = 0
        a = 0
        for r in range(len(s)):
            while s[r] in seen :
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            a = max(a,r-l+1)
        return a

        
        