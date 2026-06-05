class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Need to store longest sequeunce while doing one pass
        #Does not have to be consecutive in array
        #Identify where a seq begins if n-1 not in given array
        #Start building only if it is a start and use hash set by converting array

    
        #sort nums: 
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while(num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
            
            

      
        