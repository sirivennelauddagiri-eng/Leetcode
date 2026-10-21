class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def parenthesis(current,open_count,close_count):
            if len(current) == 2*n:
                res.append(current) 
                return
            if open_count < n:
                parenthesis(current+"(",open_count+1,close_count)
            
            if open_count > close_count:
                parenthesis(current+")",open_count,close_count+1)
        parenthesis("",0,0)
        return res
            
        