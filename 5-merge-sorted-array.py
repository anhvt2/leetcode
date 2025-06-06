class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1  # pointer for nums1
        j = n - 1  # pointer for nums2
        k = m + n - 1  # pointer for placement in nums1

        # Merge in reverse order
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any remaining in nums2, copy them over
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

nums1 = [1,2,3,0,0,0]; m = 3
nums2 = [2,5,6]; n = 3
sol = Solution()
result = sol.merge(nums1, m, nums2, n)
print(result.nums1)
