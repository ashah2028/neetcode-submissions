class Solution:
    def trap(self, height: List[int]) -> int:
        #Can get height of the containers 
        #Find max area using two pointers approach

        #start at beginning, then keep incrementing until next container is same or higher
        #for each of these can subtract box of height if non zero, and keep adding sum
        #Then move left pointer to where right is and then same tactic
        #Stop executing when right pointer  is len(height)
        #-> Does not account for if there is no container larger or same size

        #have l,r pointers
        #When you see a higher wall on right, that means the left wall useless 
        #That means you can increment until reaching a wall higher or equal to right side
        #Keep calculating left and right waters and then add after pointer meet

        l, r = 0, len(height) - 1

        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            #left less than right
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

