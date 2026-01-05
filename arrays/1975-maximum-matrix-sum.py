class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        # total: sum of absolute values of all elements
        total = 0
        
        # neg_count: count how many negative numbers appear in the matrix
        neg_count = 0
        
        # min_abs: track the smallest absolute value in the matrix
        # initialized to +infinity so any real value will be smaller
        min_abs = float('inf')

        # Iterate over every element in the matrix
        for row in matrix:
            for x in row:
                # Count negatives to determine parity later
                if x < 0:
                    neg_count += 1

                # Convert x to its absolute value
                abs_x = abs(x)

                # Add absolute value to total sum
                total += abs_x

                # Update minimum absolute value seen so far
                min_abs = min(min_abs, abs_x)

        # If the number of negative elements is odd,
        # one element must remain negative after all operations.
        if neg_count % 2 == 1:
            # To maximize the sum, we choose the smallest absolute value
            # to stay negative, which reduces total by 2 * min_abs
            total -= 2 * min_abs

        # Return the maximum achievable matrix sum
        return total
