from typing import List
import heapq

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        """
        Simulate events. For OFFLINE events, mark user offline and push (return_time, user).
        Before each event, pop from heap all users whose return_time <= current timestamp
        and mark them online again. Process MESSAGE as described:
          - "ALL": increment global_all counter (added to everyone at the end).
          - "HERE": increment ans for every currently online user.
          - otherwise: parse "idX idY ..." and increment those users.
        Events at the same timestamp must process OFFLINE before MESSAGE, so we sort by
        (timestamp, priority) with OFFLINE having higher priority (smaller second key).
        """
        # Result array
        ans = [0] * numberOfUsers
        # Online status: True = online. Initially all online.
        online = [True] * numberOfUsers

        # Min-heap of (return_timestamp, user_id) for users currently offline.
        offline_heap = []  # heap elements: (return_time, user_id)

        # Count of "ALL" messages (applies to everyone regardless of online status per spec).
        all_mentions = 0

        # Sort events by timestamp; for equal timestamps, process OFFLINE before MESSAGE.
        # We assume events are formatted like: [eventType, timestamp_str, content]
        # Use a small priority: 0 for OFFLINE, 1 for MESSAGE (so OFFLINE comes first).
        def event_priority(ev):
            typ = ev[0]
            # If other event types appear in problem they can be handled similarly; here
            # we only need OFFLINE vs MESSAGE ordering per problem description.
            return 0 if typ == "OFFLINE" else 1

        events.sort(key=lambda ev: (int(ev[1]), event_priority(ev)))

        for ev in events:
            typ, t_str = ev[0], ev[1]
            timestamp = int(t_str)

            # Bring users back online whose offline window ended at or before `timestamp`.
            while offline_heap and offline_heap[0][0] <= timestamp:
                _, user_id = heapq.heappop(offline_heap)
                online[user_id] = True

            if typ == "OFFLINE":
                # Format: ["OFFLINE", timestamp_str, userId_str]
                user_id = int(ev[2])
                # Mark offline immediately
                online[user_id] = False
                # Schedule return at timestamp + 60
                heapq.heappush(offline_heap, (timestamp + 60, user_id))

            elif typ == "MESSAGE":
                # Format: ["MESSAGE", timestamp_str, content_str]
                content = ev[2]
                if content == "ALL":
                    # Count globally, add to every user at the end (cheaper than updating all now).
                    all_mentions += 1
                elif content == "HERE":
                    # Give +1 to every currently online user.
                    # This is O(numberOfUsers) per HERE message in worst-case.
                    for uid in range(numberOfUsers):
                        if online[uid]:
                            ans[uid] += 1
                else:
                    # Explicit list of mentions like "id1 id0 id12"
                    # Parse each "idX" -> X and increment.
                    parts = content.split()
                    for part in parts:
                        # part format guaranteed as "id<index>" per problem statement
                        uid = int(part[2:])
                        ans[uid] += 1

            else:
                # (If the problem later includes other event types, handle them here.)
                pass

        # After processing all events, add "ALL" counts to each user
        if all_mentions:
            for uid in range(numberOfUsers):
                ans[uid] += all_mentions

        return ans
