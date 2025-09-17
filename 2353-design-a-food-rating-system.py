from typing import List, Dict, Tuple
import heapq

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # food -> (cuisine, rating)
        self.info: Dict[str, Tuple[str, int]] = {}
        # cuisine -> heap of (-rating, name)
        self.heaps: Dict[str, List[Tuple[int, str]]] = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.info[f] = (c, r)
            if c not in self.heaps:
                self.heaps[c] = []
            heapq.heappush(self.heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        c, _ = self.info[food]
        self.info[food] = (c, newRating)
        heapq.heappush(self.heaps[c], (-newRating, food))  # lazy insert

    def highestRated(self, cuisine: str) -> str:
        h = self.heaps[cuisine]
        while h:
            neg_r, name = h[0]
            # Check against current rating; pop stale entries
            if self.info[name] == (cuisine, -neg_r):
                return name
            heapq.heappop(h)
        return ""  # should not happen per problem constraints


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)