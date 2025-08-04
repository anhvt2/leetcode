import bisect

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.seats = []  # sorted list of occupied seats

    def seat(self) -> int:
        # (1) Initialize: no one -> take first seat
        if not self.seats:
            self.seats.append(0)
            return 0

        # (2) Otherwise, find the largest gap
        max_dist = self.seats[0]            # distance if we sit at 0
        seat = 0

        # (3) Check middle positions between adjacent seats
        for i in range(len(self.seats) - 1):
            prev, nxt = self.seats[i], self.seats[i+1]
            d = (nxt - prev) // 2
            if d > max_dist:
                max_dist = d
                seat = prev + d

        # (4) Check the end (n-1)
        if self.n - 1 - self.seats[-1] > max_dist:
            max_dist = self.n - 1 - self.seats[-1]
            seat = self.n - 1

        # (5) Insert/record the new seat while mainting sorting self.seats and return seat
        bisect.insort(self.seats, seat)
        return seat

    def leave(self, p: int) -> None:
        # Remove seat p from the sorted list
        self.seats.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)