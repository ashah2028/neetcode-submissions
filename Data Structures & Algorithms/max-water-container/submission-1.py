class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force = go through each combination O(n^2) and compute max area
        #Optimal approach is top use two pointers & decrease for side with lower height
        #and calculate area each time

        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            currArea = min(heights[l], heights[r]) * (r-l)
            area = max(area, currArea)
            if (heights[r] < heights[l]):
                r -= 1
            else:
                l += 1
        return area

        
  





        