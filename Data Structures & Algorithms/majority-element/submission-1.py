class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #can count frequencies, but would require extra space due to hashmap
        #need a map of int counts

        counts = defaultdict(int)
        
        #calculate what majority val is n/2 + 1
        maj_val = len(nums) // 2 + 1

        #loop through array each num
        for num in nums: 
            #if counts[num] + 1 == maj_val, then return num
            if counts[num] + 1 == maj_val:
                return num
            counts[num] += 1
        
        #beter code design is to have a res and return that res


        #for O(1)
        #bit manipulation LOL?