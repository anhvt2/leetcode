class Robot:
    def __init__(self, width, height):
        """
        Key idea:
        - Precompute the entire perimeter path in order.
        - Store for each step:
            ((x, y), direction_at_that_position)
        - Then step() becomes simple modular indexing.

        Path order (clockwise):
            bottom row → right column → top row → left column
        """

        # perimeter_path[k] = ((x, y), direction when standing here)
        self.perimeter_path = [((0, 0), "South")]
        # IMPORTANT:
        # - Problem defines that at origin BEFORE any move, direction is "East"
        # - But AFTER completing a full cycle back to (0,0), direction becomes "South"
        # - So we initialize origin direction as "South" and fix it via `is_at_origin` later

        # bottom edge: (0,0) → (width-1,0), moving East
        for i in range(1, width):
            self.perimeter_path.append(((i, 0), "East"))

        # right edge: (width-1,0) → (width-1,height-1), moving North
        for j in range(1, height):
            self.perimeter_path.append(((width - 1, j), "North"))

        # top edge: (width-1,height-1) → (0,height-1), moving West
        for i in range(width - 2, -1, -1):
            self.perimeter_path.append(((i, height - 1), "West"))

        # left edge: (0,height-1) → (0,0), moving South
        # NOTE: we stop at j=1 to avoid duplicating (0,0)
        for j in range(height - 2, 0, -1):
            self.perimeter_path.append(((0, j), "South"))

        # current index in the perimeter cycle
        self.current_idx = 0

        # special flag:
        # - True only before any step() is called
        # - needed to override direction at origin
        self.is_at_origin = True

    def step(self, num):
        """
        - Move forward `num` steps along the perimeter cycle
        - Use modulo to wrap around (cycle behavior)
        """

        self.is_at_origin = False  # once we move, no longer initial state

        # advance index cyclically
        self.current_idx = (self.current_idx + num) % len(self.perimeter_path)

    def getPos(self):
        """
        - Return current (x, y)
        - O(1) lookup from precomputed list
        """
        return self.perimeter_path[self.current_idx][0]

    def getDir(self):
        """
        - Return current direction

        Special case:
        - At the very beginning (before any step), robot is at (0,0) facing "East"
        - But in our precomputation, (0,0) is stored with "South"
        - So we override using `is_at_origin`
        """

        return "East" if self.is_at_origin else self.perimeter_path[self.current_idx][1]