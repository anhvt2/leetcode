from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        1. Count frequencies of each task (A-Z)
        2.  `max_freq`: highest frequency
            `max_count`: how many tasks have `max_freq` frequency
        3. Form `frame` by the most frequent tasks has length
            frame = (max_freq - 1) * (n+1) + max_count
        4. Solution = max(frame, number of tasks). If there are enough tasks, then should not be idle.
        """
        # Count task frequencies
        freq = Counter(tasks)
        max_freq = max(freq.values())
        # Count how many tasks that has max_freq
        max_count = sum(1 for v in freq.values() if v == max_freq)

        # Compute frame size
        part_count = max_freq - 1
        part_length = n + 1
        frame = part_count * part_length + max_count

        # Solution
        return max(frame, len(tasks))
