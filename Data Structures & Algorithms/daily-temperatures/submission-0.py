class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Enumerate through the array, stack appending tuple (count, temp)
        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                res[stackIndex] = index - stackIndex
            stack.append((temp, index))
        return res

                

            

            
            


        