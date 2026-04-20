class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Remove consecutive duplicates
        arr = [nums[0]] # init
        for num in nums[1:]:
            if num != arr[-1]:
                arr.append(num)

        count = 0
        for i in range(1, len(arr) - 1):
            if  arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                count += 1 # hill
            elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                count += 1 # valley
        
        return count
