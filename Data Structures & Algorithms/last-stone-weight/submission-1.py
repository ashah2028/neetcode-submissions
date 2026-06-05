class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Turn it into a max heap by making list negated and heapify
        #At each step pop the two heaviest stones, then based off conditions
        # put the stone leftover if x < y back into the heap
        #kEep doing this while heap has > 1 stone 
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0])