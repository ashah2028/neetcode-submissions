class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, lst, currVal):
            if (currVal == target):
                res.append(lst.copy())
                return
            if index >= len(nums) or currVal > target:
                return
            lst.append(nums[index])
            dfs(index, lst, currVal + nums[index])
            lst.pop()
            dfs(index + 1, lst, currVal)

        dfs(0, [], 0)
        return res

        
    