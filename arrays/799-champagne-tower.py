class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Start with all champagne poured into the top glass (row 0, glass 0)
        # curr[i] = total amount of champagne in glass i of the current row
        # Note: glasses can temporarily hold >1 before overflow
        curr = [poured]
        
        # Simulate pouring row by row from row 0 to query_row-1
        # Each iteration calculates the next row based on overflow from current row
        for row in range(query_row):
            # Row N has N+1 glasses (row 0 has 1, row 1 has 2, etc.)
            # So next row (row+1) has row+2 glasses
            next_row = [0.0] * (row + 2)
            
            # Process each glass in current row
            for i in range(len(curr)):
                # Each glass can hold max 1.0 unit
                # If glass has >1.0, the excess overflows down
                if curr[i] > 1:
                    overflow = curr[i] - 1
                    # Overflow splits equally to two children:
                    next_row[i] += overflow / 2      # left child (same index)
                    next_row[i + 1] += overflow / 2  # right child (index+1)
            
            curr = next_row
        
        # After simulation, curr is the query_row
        # Return min(1.0, amount) since glass capacity is 1.0
        return min(1, curr[query_glass])