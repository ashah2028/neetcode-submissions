class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sum has to equal 0. We can use a sorted array, and 
        #loop through it to get if = 0 for any index
        #for each index use a 2 pointer approach where 
        #the pointers move based off the triplet's value
        #skip over while first index is same # as prev
        #to avoid writing duplicates
        #also skip over the 2nd # that is the same when iterating

        res = []
        nums.sort()
        #
        for i, num in enumerate(nums): 

            #if pos, stop looping
            if num > 0:
                break

            #if same as prev index
            if i >0 and nums[i-1] == nums[i]:
                continue
            
            #two pointers exploration 
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else: 
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    
                    #second number is same
                    while nums[l-1] == nums[l] and l < r: 
                        l += 1
        return res


       