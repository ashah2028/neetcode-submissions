class MyStack:

    def __init__(self):
        self.queue = deque()

        

    def push(self, x: int) -> None:
        #need to rotate elements
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            elem = self.queue.popleft()
            self.queue.append(elem)

        

    def pop(self) -> int:
        return self.queue.popleft()
        

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()