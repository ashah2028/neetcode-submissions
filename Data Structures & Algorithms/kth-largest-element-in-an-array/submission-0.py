class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Use a max heap 
        nums = [-n for n in nums]
        heapq.heapify(nums)
        high = 0
        #Keep popping while K > 0
        while k > 0 and nums:
            high = heapq.heappop(nums)
            k -= 1
        return high * -1