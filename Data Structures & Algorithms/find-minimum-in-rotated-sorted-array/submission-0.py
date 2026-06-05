class Solution:
    def findMin(self, nums: List[int]) -> int:
        #Pointers l&r 
        #MP l + (r-l)/2
        #Binary Search
        l, r = 0, len(nums) - 1
        #arbitrary does not matter
        res = nums[0]

        while l <= r:   
            #If sub array is sorted then go through this
            if nums[l] < nums[r]: 
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            #Search right
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


