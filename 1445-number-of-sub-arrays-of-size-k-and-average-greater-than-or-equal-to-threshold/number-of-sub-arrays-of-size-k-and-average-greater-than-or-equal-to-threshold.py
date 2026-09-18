class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        s1 = sum(arr[:k])
        c = 0
        if s1 >= threshold*k:
            c += 1
        for i in range(k,len(arr)):
            s1 += arr[i]
            s1 -= arr[i-k]
            if s1/k >= threshold:
                c += 1
        return c

            
        