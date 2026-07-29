class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #use stack to store scores

        #maybe pop last two when needed and then push back on w new score

        stack = []
        sum_scores = 0
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
                sum_scores += stack[-1]
            elif op == 'D':
                stack.append(stack[-1] * 2)
                sum_scores += stack[-1]
            elif op == 'C':
                elem = stack.pop()
                sum_scores -= elem
            else:
                stack.append(int(op))
                sum_scores += int(op)
        
        return sum_scores

        