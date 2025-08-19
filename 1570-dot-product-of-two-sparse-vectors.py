class SparseVector:
    def __init__(self, nums: List[int]):
        self.data = {i: num for i, num in enumerate(nums) if num != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # if len(self.data) > len(vec.data):
        #     return vec.dotProduct(self)
        sum = 0
        for i in self.data:
            if i in vec.data:
                sum += self.data[i] * vec.data[i]
        return sum

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
