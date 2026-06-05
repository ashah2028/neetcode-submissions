class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # One pass solution 
        preVals = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in preVals:
                return [preVals[diff], i]
            preVals[n] = i
        