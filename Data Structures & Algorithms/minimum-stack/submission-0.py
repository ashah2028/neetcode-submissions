class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        # Two stacks for getMin

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        # if stack is not empty, compare to min of last 
        # element of stack or else val and val


    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
