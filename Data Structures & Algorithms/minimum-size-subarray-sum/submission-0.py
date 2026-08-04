class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #subarray is contigious -> need to slide and look if it meets target
        #[2,2,2,2,4] target = 6
        #Can slide left pointer when we reach a subarray winodw >= target
        #O(n) time O(1) space needed

        #solution

        #left pointer, result, sub_sum
        res = float('inf')
        l = 0
        sub_sum = 0
        #for r in nums
        for r in range(len(nums)):
            #put value in sub_sum
            sub_sum += nums[r]
            #while sum >= target
            while sub_sum >= target:
                #calc res from window length using max
                res = min(res, r - l + 1)
                #subtract left from sub_sum
                sub_sum -= nums[l]
                #incr left pointer
                l += 1
        #return result
        if res == float('inf'):
            return 0
        return res