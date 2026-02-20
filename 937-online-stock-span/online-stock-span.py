class StockSpanner:

    def __init__(self):
        self.stk = []
        self.day = 0

    def next(self, price: int) -> int:
        self.day += 1
        if not self.stk or self.stk[-1][0] > price:
            self.stk.append((price, self.day))
            return 1
        while self.stk and self.stk[-1][0] <= price:
            self.stk.pop()
        res = self.day if not self.stk else self.day - self.stk[-1][1]
        self.stk.append((price, self.day))
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)