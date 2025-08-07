class Vector2D:
    def __init__(self, vec: List[List[int]]):
        self.flat = []
        for v in vec:
            for n in v:
                self.flat.append(n)
        self.id = 0

    def next(self) -> int:
        self.id += 1
        return self.flat[self.id - 1]

    def hasNext(self) -> bool:
        return self.id < len(self.flat)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()