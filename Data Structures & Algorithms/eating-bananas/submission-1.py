class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Sorted search space from 1 - max(piles)
        #Use divison to figure out smallest speed: 
        #the totaltime is .ceil(pile/speed)
        #if totaltime <= h then reached bare minimum (edge case)
        #instead of iterating via each pile (brute force)
        #binary search is to compute curr speed using mp
        #if within allowed time h, speed works search lower
        #if less than h search upper

        l, r = 1, max(piles)
        tot = r
        while l <= r:
            m = l + (r-l) // 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / m)
            if totalTime <= h:
                tot = m
                r = m - 1
            else:
                l = m + 1
        return tot




        
        