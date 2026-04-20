import random
class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}  # maps value to its index in the list
        self.values = []        # list of values

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # Move the last element to the index of the one to delete
        last_val = self.values[-1]
        idx = self.val_to_index[val]
        self.values[idx] = last_val
        self.val_to_index[last_val] = idx
        # Remove last element
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

# import random
# class RandomizedSet:

#     def __init__(self):
#         self.set = set()

#     def insert(self, val: int) -> bool:
#         if val not in self.set:
#             self.set.add(val)
#             return True
#         else:
#             return False

#     def remove(self, val: int) -> bool:
#         if val in self.set:
#             self.set.remove(val)
#             return True
#         else:
#             return False

#     def getRandom(self) -> int:
#         return random.choice(list(self.set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()