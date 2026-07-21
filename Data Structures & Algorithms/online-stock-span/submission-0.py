class StockSpanner:

    def __init__(self):
        self.stack = [] #(price, span)


        

    def next(self, price: int) -> int:
        #keep popping stack while lower or same
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, span))
        return span

#[100, 80, 60, 70, 60, 75, 85] -> [1, 1, 1, 2, 1, 4, 6]
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

#problem: need to reference the past nums but can just keep adding spans

