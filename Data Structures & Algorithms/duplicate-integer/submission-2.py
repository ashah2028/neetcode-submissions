class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Can use freq count with a freqmap
        #Since each key can only have a value <= 1,
        #if the value of the key is larger, then the int array
        #contains a duplicate 

        #Freqmap - using defaultdict so that each new key has a value of 0

        freqMap = defaultdict(int)

        #iterate through nums
        for num in nums:
            #If num's freq already =1, return true
            if freqMap[num] == 1:
                return True
            #Dont have to worry abt bindings because each key has default 0 val
            freqMap[num] += 1
        #no duplicate
        return False


        