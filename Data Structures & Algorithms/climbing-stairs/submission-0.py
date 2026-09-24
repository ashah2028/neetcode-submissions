class Solution:
    def climbStairs(self, n: int) -> int:
        #different choices which can be taking the 1 or 2 steps
        #Build out a reccurance relationship

        #each i given a choice, 1 or 2 steps
        #build a storage of the results of recursive calls to memoize the solution

        #recursive solution 
        cache = [-1] * n
        def dfs(i):
            #compute if valid path or not
            if i >= n:
                return i == n
            #check cache for the result
            if cache[i] != -1:
                return cache[i]
            #cache the result
            cache[i] = dfs(i+1) + dfs(i+2)
            return cache[i]

        return dfs(0)    




        