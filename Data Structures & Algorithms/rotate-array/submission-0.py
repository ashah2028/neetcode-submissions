class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #K single roatations O(n*k)

        #Use extra space array O(n) to map positions
        #arr = [nums[3], nums[1], nums[2], nums[0]]
        #going to require 2 passese

        arr = [0] * len(nums)

        #computing indexes = i + k % n
        #k = 2, n = 4
        #arr = [2, 3, 0, 1]
        for i in range(len(nums)):
            arr[(i + k) % len(nums)] = nums[i]
        
        #have positions now need to map!
        nums[:] = arr
        