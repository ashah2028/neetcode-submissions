class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        #sorted nums 
        nums.sort()

        #i is index of nums
        def dfs(i):
            #base case
            if i == len(nums):
                res.append(subset.copy())
                return

            #include
            subset.append(nums[i])
            #no dups so +1 - cannot reuse to avoid duplicate sets
            dfs(i + 1)
            #exclude
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i + 1)

        #run dfs & return result
        dfs(0)
        return res



