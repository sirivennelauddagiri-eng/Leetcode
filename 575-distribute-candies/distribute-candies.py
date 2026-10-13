class Solution(object):
    def distributeCandies(self, candyType):
        mp = {}
        for i in candyType:
            if i not in mp:
                mp[i] = 1
            else:
                mp[i] += 1
        return min(len(mp),len(candyType)//2)


            
