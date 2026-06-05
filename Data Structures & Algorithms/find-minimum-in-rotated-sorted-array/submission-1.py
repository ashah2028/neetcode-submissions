class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Rotated array means bitmask shift >> 
        #max rotation is len of nums 
        #To find point of rotation need to find where array does not increase
        #This would take O(n) worst case
        #For O(logn) time can use a binary search approach
        #Since one part sorted and one contains rotation + min

        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = l + (r-l) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid -1
        return res




