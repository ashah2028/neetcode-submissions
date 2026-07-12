class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Two pointer pass without space 

        #[3, 2, 1, 4, 5, 6]
        #i = 0, k = len(nums) - 1
        i, n = 0, len(nums)
        
        #while i <= k: *edge case
        while i < n: 
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i+= 1

        return n

        #if same need to swap, deincrement k, but not i cause need to check

        #else, increment i 

        #return k at end


        #edge case: when i = k, if nums[i] is val 