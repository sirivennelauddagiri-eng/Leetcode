class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = nums1[:m]
        j = nums2[:n]
        k = i+j
        k.sort()
        nums1[:] = k
        