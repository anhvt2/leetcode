class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        res = []

        # For the "I" version (n, nums[i] <= 50), a direct recompute per window is fine.
        for i in range(n - k + 1):
            window = nums[i:i+k]
            cnt = Counter(window)

            # Sort keys by (-frequency, -value) to respect the tie-break rule.
            top_vals = sorted(cnt.keys(), key=lambda v: (-cnt[v], -v))[:x]

            # Sum only contributions from the selected values
            keep = set(top_vals)
            total = sum(v for v in window if v in keep)
            res.append(total)

        return res