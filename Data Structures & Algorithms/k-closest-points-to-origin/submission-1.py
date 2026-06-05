class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Need to create an array to keep all the distances and their og indexex
        #Can sort array and return lowest k's indexes
        #Loop through points list for each of the k indexes O(nlogn)

        #For a more optimal approach can use a max heap while iterating through
        #Once > k elements in the heap can remove the max element/furthest. After iteration, 
        #heap contains the points and convert to array and return it

        maxHeap = []
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            
        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
            
        return res
