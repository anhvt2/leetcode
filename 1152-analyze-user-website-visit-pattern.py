from collections import defaultdict
import heapq

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        heap = []
        patterns = defaultdict(int)
        users = defaultdict(list)
        maxc = 0
        maxp = ""

        for i in range(len(website)):
            heapq.heappush(heap, (timestamp[i], username[i], website[i]))

        while heap:
            t, u, w = heapq.heappop(heap)
            users[u].append(w)

        for u, w in users.items():
            visited = set()
            
            for i in range(len(w)):
                for j in range(i+1, len(w)):
                    for k in range(j+1, len(w)):
                        p = (w[i], w[j], w[k])

                        if p in visited:
                            continue

                        visited.add(p)
                        patterns[p] += 1

        for p, cnt in patterns.items():
            if cnt > maxc or (cnt == maxc and p < maxp):
                maxc = cnt
                maxp = p

        return list(maxp)

sol = Solution()
username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
print(sol.mostVisitedPattern(username, website, timestamp))

