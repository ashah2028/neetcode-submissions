class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Create freq map
        freqMap = defaultdict(int)

        #freq groups initalization (max amount): 
        freq = [[] for i in range(len(nums) + 1)]

        #Iterate nums
        for num in nums:
            freqMap[num] += 1

        #Put into the freq groups
        for bind in freqMap:
            frequency = freqMap[bind]
            freq[frequency].append(bind)
        
        #res
        res = []

        #Get frequencies starting from highest range(start, stop, step)
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
