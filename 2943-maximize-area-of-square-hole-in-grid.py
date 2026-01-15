class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
        # Helper function to compute longest consecutive run
        def longest_consecutive(bars: list[int]) -> int:
            if not bars:
                return 1  # no bars removed → 1 unit
            
            bars.sort()
            longest = 1
            current = 1

            for i in range(1, len(bars)):
                if bars[i] == bars[i - 1] + 1:
                    current += 1
                    longest = max(longest, current)
                else:
                    current = 1

            # +1 because k consecutive removed bars create k+1 merged cells
            return longest + 1

        # Maximum possible height and width
        max_height = longest_consecutive(hBars)
        max_width = longest_consecutive(vBars)

        # Square side length
        side = min(max_height, max_width)

        return side * side
