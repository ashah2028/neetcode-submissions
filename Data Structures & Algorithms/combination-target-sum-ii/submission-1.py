class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(index, lst, currVal):
            if currVal == target:
                res.append(lst.copy())
                return
            if index == len(candidates) or currVal > target:
                return
            
            lst.append(candidates[index])
            dfs(index + 1, lst, currVal + candidates[index])
            lst.pop()
            
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index + 1, lst, currVal)

        dfs(0, [], 0)
        return res






