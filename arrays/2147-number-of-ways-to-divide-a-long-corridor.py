class Solution:
    def numberOfWays(self, corridor: str) -> int:
        """
        Algorithm:
        ----------
        We want to divide the corridor into sections such that each section
        contains exactly two seats ('S').

        Step 1: Count the total number of seats.
            - If the total number of seats is 0 or odd, return 0 immediately,
              because it is impossible to form valid sections.

        Step 2: Traverse the corridor from left to right while tracking:
            - seat_count: total number of seats seen so far
            - plant_count: number of plants ('P') after completing a 2-seat section
            - ways: running product of valid divider placements

        Step 3:
            - Every time we finish a section of two seats and later encounter
              the first seat of the next section, the number of places where a
              divider could have been placed equals (plant_count + 1).
            - Multiply ways by (plant_count + 1), reset plant_count, and continue.

        Step 4: Return the final number of ways modulo 1e9 + 7.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        MOD = 10**9 + 7

        total_seats = corridor.count('S')
        if total_seats == 0 or total_seats % 2 != 0:
            return 0

        ways = 1
        seat_count = 0
        plant_count = 0

        for c in corridor:
            if c == 'S':
                seat_count += 1

                # When starting a new section (after the first two seats),
                # multiply by the number of divider choices
                if seat_count > 2 and seat_count % 2 == 1:
                    ways = (ways * (plant_count + 1)) % MOD
                    plant_count = 0
            else:  # c == 'P'
                # Count plants only after completing a section
                if seat_count >= 2 and seat_count % 2 == 0:
                    plant_count += 1

        return ways
