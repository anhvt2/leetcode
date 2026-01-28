class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('+inf')
        n = len(arr)
        ans = []
        for i in range(n-1):
            curr_diff = arr[i+1] - arr[i]
            if curr_diff < min_diff:
                ans = []
                ans.append([arr[i], arr[i+1]])
                min_diff = curr_diff
            elif curr_diff == min_diff:
                ans.append([arr[i], arr[i+1]])
        return ans