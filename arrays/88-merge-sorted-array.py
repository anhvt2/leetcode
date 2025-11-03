class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
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
