    class Fancy:

        def __init__(self):
            self.arr = []
            self.add = 0
            self.mul = 1
            self.MOD = 10**9 + 7

        def append(self, val: int) -> None:
            self.arr.append((val, self.add, self.mul))

        def addAll(self, inc: int) -> None:
            self.add = (self.add + inc) % self.MOD

        def multAll(self, m: int) -> None:
            self.mul = (self.mul * m) % self.MOD
            self.add = (self.add * m) % self.MOD

        def getIndex(self, idx: int) -> int:
            if idx >= len(self.arr):
                return -1
            val, add, mul = self.arr[idx]
            mul_2 = self.mul * pow(mul, self.MOD - 2, self.MOD) % self.MOD
            add_2 = (self.add - add * mul_2) % self.MOD
            return (val * mul_2 + add_2) % self.MOD

    # Your Fancy object will be instantiated and called as such:
    # obj = Fancy()
    # obj.append(val)
    # obj.addAll(inc)
    # obj.multAll(m)
    # param_4 = obj.getIndex(idx)