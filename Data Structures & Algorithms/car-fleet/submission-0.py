class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #create a merged list of (pos, speed) tuples 
        pairs = []
        #Position and speed have the same length
        for i in range(len(position)):
            pair = (position[i], speed[i])
            pairs.append(pair)
        #Time to get to target can be initalized to 0 because no car has 0 time
        fleets = curTime = 0
        #Reverse pairs to go from highest pos to lowest
        for p, s in sorted(pairs, reverse = True):
            #Calc time to target
            desTime = (target - p)/s
            #if next car is less time to target, it will become fleet with slower one
            #if next car is more time to target, it becomes a new fleet and the time of fleet
            #for next cars becomes this fleets time. 
            if curTime < desTime: 
                fleets += 1
                curTime = desTime
        return fleets






        