class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # time: O(n), space: O(1)
        # Whenever there is a run of consecutive ballons with same color, then we must remove all except for 1
        # For each run, pay the sum of its `neededTime` minus the maximum in that run
        ans = 0
        i, n = 0, len(colors)
        while i < n:
            j = i
            run_sum = 0
            run_max = 0
            while j < n and colors[j] == colors[i]:
                run_sum += neededTime[j]
                run_max = max(run_max, neededTime[j])
                j += 1
            # keep the most expensive one in the run
            ans += (run_sum - run_max)
            i = j
        return ans