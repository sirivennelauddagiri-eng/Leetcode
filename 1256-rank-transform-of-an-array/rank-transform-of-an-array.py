class Solution(object):
    def arrayRankTransform(self, arr):
       sort_arr = sorted(set(arr))
       rank = {}
       for i in range(len(sort_arr)):
            rank[sort_arr[i]] = i+1
       for i in range(len(arr)):
            arr[i] = rank[arr[i]]
       return arr
