class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """
        Algorithm:
        ----------
        1. Assume the shop closes at time 0 (always closed).
           Initial penalty = number of 'Y' (missed customers).
        2. Move closing time from left to right.
           - If we pass a 'Y', penalty decreases by 1.
           - If we pass an 'N', penalty increases by 1.
        3. Track the minimum penalty and earliest closing time.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        # Initial penalty: all 'Y' are missed
        penalty = customers.count('Y')

        min_penalty = penalty
        best_time = 0

        # Move closing time forward
        for i, c in enumerate(customers):
            if c == 'Y':
                penalty -= 1   # now served
            else:
                penalty += 1   # unnecessary open day

            # Closing time is i + 1
            if penalty < min_penalty:
                min_penalty = penalty
                best_time = i + 1

        return best_time
