class Solution(object):
    def reverseDegree(self, s):
        ans = 0
        for i in range(len(s)):
            v = 26-(ord(s[i])-ord('a'))
            ans += v*(i+1)
        return ans