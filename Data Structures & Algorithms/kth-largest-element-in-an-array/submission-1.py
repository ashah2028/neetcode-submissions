class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #store k largest elements sean
        minHeap = []
        for num in nums: 
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]

        


        