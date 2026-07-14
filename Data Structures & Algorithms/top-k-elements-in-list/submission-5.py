class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Edge cases [], [7, 7] k = 2

        #Approach -> use hashmap to store frequencies and then sort based on vals and take last k entries
        # Result: O(n) space and O(nlogn) runtime due to sorting

        #More optimal -> utilize min-heap with frequencies after iteration and when it grows higher than k pop lowest amount
        #Result: O(n) space for heap and O(logn) for heapify and O(n) runtime for list iteration
        #Need to track frequencies as well -> hashmap

        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        #Heap
        heap = []
        for num in counts.keys():
    #       add it in then pop
            heapq.heappush(heap, (counts[num], num))
            #if too large, pop
            if len(heap) > k:
                heapq.heappop(heap)

        #result
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        


