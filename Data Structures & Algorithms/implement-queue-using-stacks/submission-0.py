class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        

    def push(self, x: int) -> None:
        #need two stacks 
        #can add all elements except bottom to one stack
        #then just pop back into stack 1
        #s1 = [1, 2, 3] x = 4 s2 = [3, 2, 1] s1 = [4] -> [4, 1, 2 ,3]
        for _ in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(x)
        for _ in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())


    def pop(self) -> int:
        return self.stack1.pop()
        

    def peek(self) -> int:
        return self.stack1[-1]
        

    def empty(self) -> bool:
        return not self.stack1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()