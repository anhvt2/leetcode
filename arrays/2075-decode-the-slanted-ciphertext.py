class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        """
        Key idea:
        - The text was written row-wise into a matrix with `rows` rows.
        - Then encoded by reading diagonals: (r, c) -> (r+1, c+1).
        - Number of columns = len(encodedText) // rows

        Reconstruction:
        - Build implicit matrix index mapping (no need to actually build matrix)
        - For each starting column c in first row:
            walk diagonally down-right and collect characters

        - Finally, strip trailing spaces (as per problem requirement)
        """

        if rows == 1:
            return encodedText.rstrip()

        n = len(encodedText)
        cols = n // rows

        res = []

        # Start from each column in the first row
        for c in range(cols):
            r, j = 0, c

            # Walk diagonally
            while r < rows and j < cols:
                res.append(encodedText[r * cols + j])
                r += 1
                j += 1

        # Remove trailing spaces
        return "".join(res).rstrip()