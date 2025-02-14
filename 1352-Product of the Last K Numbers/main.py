class ProductOfNumbers:

    def __init__(self):
        self.r = []
        self.total = 1

    def add(self, num: int) -> None:
        if num == 0:          
            self.__init__()
        else:        
            self.total *= num
            self.r.append(self.total / num) 
        

    def getProduct(self, k: int) -> int:
        if k > len(self.r):
            return 0
        else:
            return int(self.total // self.r[-k])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)