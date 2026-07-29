class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        #amortize 2 stacks
        self.stack1.append(x)


    def pop(self) -> int:
        #pop all of stack,
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

        #[4,5,6] -> [6,5,4]
        

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        
        

    def empty(self) -> bool:
        return max(len(self.stack1), len(self.stack2)) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()