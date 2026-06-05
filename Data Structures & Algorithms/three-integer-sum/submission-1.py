class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Brute force would be O(n^3)
        #Sort array O(nlogn)
        #Use two sum approach where the third val = - (j + k)
        #Since sorted use 2 pointers from where index is and move them based off if less or more than target
        #for duplicates while last num same as prev increment left pointer

        res = []
        nums.sort()

        #Enumerate through each num (i)
        for i, a in enumerate(nums):

            #a must be positive
            if a > 0:
                break

            #if = prev index term skip it
            if i > 0 and a == nums[i-1]:
                continue
            
            #using 2 pointers 
            l, r = i + 1, len(nums) - 1
            
            #loop pointers
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res

        