class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use a HashMap with the (target-val@index, index)
        #If target - val at current index is a key in map:
        #Return key's value (index) and current index, by whichever index smaller

        #Map
        DiffMap = {}
        #Go through each num:
        for i, n in enumerate(nums):
            #If the other val needed to get target in map
            if ((target - n) in DiffMap):
                #Smaller index first
                return [DiffMap[target-n], i]
            DiffMap[n] = i
            


        