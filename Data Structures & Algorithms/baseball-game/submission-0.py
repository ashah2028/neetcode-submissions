class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #use stack to store scores

        #maybe pop last two when needed and then push back on w new score

        stack = []

        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        sum_scores = 0

        while stack:
            sum_scores += stack.pop()
        
        return sum_scores

        