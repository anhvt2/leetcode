import collections
import heapq

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
# reduce largest elements in diffs at most k1+k2 times
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2) if n1 != n2]
        k = k1 + k2
        if k >= sum(diffs):
            return 0

        # Group identical diff values to avoid O(k log n) behavior.
        # counter[v] = how many positions currently have diff == v.
        counter = collections.Counter(diffs)
        # We want to repeatedly reduce the LARGEST diffs first.
        # Python has a min-heap, so push (-diff, freq) to simulate a max-heap by value.
        nums = [[-diff, freq] for diff, freq in counter.items()]
        heapq.heapify(nums)

        # Keep spending k while we still have positive diffs
        while k > 0 and nums and nums[0][0] != 0:
            # Pop the current largest diff "level"
            val, freq = heapq.heappop(nums)
            # Convert back to positive diff value
            val = -val
            # Look at the next largest level to "flatten" down to, or 0 if None
            target = -nums[0][0] if nums else 0
            
            # We want to move 'freq' items from 'val' down to 'target'
            # If a target bucket already exists at the top, just add the frequency
            if (val - target) * freq <= k:
                # We have enough k to fully flatten this level to 'target'
                k -= (val - target) * freq

                # After flattening, all these 'freq' counts will join the 'target' bucket
                # If a target bucket already exists as the top, then just add the frequency
                if nums:
                    nums[0][1] += freq
                # (If target == 0 and nums is empty or next top is smaller, will will just stop in the next iteration since top diffs == 0 end the loops)
            else:
                # Not enough k to reduce every val to target
                # Split [val, freq] into 
                #   [val - k // freq, freq]
                #   [val - k // freq - 1, k - k // freq * freq]
                reduced = k // freq
                remainder = k % freq

                heapq.heappush(nums, [-(val - reduced), freq - remainder])
                if remainder > 0:
                    heapq.heappush(nums, [-(val - reduced - 1), remainder])
                
                k = 0

        res = 0
        for val, freq in nums:
            res += val * val * freq
        return res