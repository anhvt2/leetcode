# class Solution:
#     def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
#         # Build a list of (distance, value) pairs for value in arr
#         dist_pairs = [(abs(a - x), a) for a in arr]
#         # Sort by distances first, then by value for tie-break
#         dist_pairs.sort(key=lambda p: (p[0], p[1]))
#         # Extract the first k elements, then sort
#         first_k = [a for _, a in dist_pairs[:k]]
#         return sorted(first_k)

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # We're going to choose a window of length k
        # by its starting index `left` in the range [0, len(arr) - k].
        left, right = 0, len(arr) - k

        # Binary search to find the smallest `left` such that
        # the k-element window [left, left + k) is as close to x as possible.
        while left < right:
            mid = (left + right) // 2

            # Compare the two "edge" distances for the window starting at mid:
            #   - distance from x to the left end:  x - arr[mid]
            #   - distance from x to the right end: arr[mid + k] - x
            #
            # If the left end is farther away than the right end,
            # it means shifting the window right (increasing left) could yield a closer group.
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                # Otherwise, the window starting at mid is at least as good as
                # any window to its right, so we keep it or move left.
                right = mid

        # Return the optimal window
        return arr[left : left+k]
