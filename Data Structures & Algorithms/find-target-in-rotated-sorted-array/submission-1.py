class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Wherever the dip is where the array is partioned into 2 sorted arrays
        #edge cases: nums is empty, neg numbers, target is piv min or max

        #start with a binary search 
        l, r = 0, len(nums) - 1

        # <= because minimum and maximum count too
        while l <= r:
            m = l + (r-l) // 2

            #if mid is target
            if nums[m] == target:
                return m

            # if left less than mid
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else: 
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return - 1

                
