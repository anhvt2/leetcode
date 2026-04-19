class Solution:
    def maxDistance(self, nums1, nums2):
        """
        Two pointers on non-increasing arrays:
        - If nums1[i] <= nums2[j]: valid → update answer, move j
        - Else: move i
        """

        i = j = 0
        ans = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                ans = max(ans, j - i)
                j += 1
            else:
                i += 1

        return ans