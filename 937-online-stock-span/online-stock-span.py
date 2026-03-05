class StockSpanner:

    def __init__(self):
        self.stk = [] # d, price

    def next(self, price: int) -> int:
        days = 1
        while self.stk and self.stk[-1][1] <= price:
            d, _ = self.stk.pop()
            days += d
        self.stk.append((days, price))
        return days
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)