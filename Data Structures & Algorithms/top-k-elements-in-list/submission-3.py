class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Store the freq of each num in dict
        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
        #Create a min-heap 
        #In heap store the freq and the values with that freq
        heap = [] 

        for num in freqMap.keys():
            heapq.heappush(heap, (freqMap[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

       
