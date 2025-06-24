from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # Build graph and in-degree count
        for dest, src in prerequisites:
            graph[src].append(dest)
            in_degree[dest] += 1

        # Initialize queue with nodes having in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited_courses = 0

        while queue:
            course = queue.popleft()
            visited_courses += 1
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return visited_courses == numCourses


# from typing import List
# from collections import defaultdict

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

#         # Build adjacency list
#         graph = defaultdict(list)
#         for dest, src in prerequisites:
#             graph[src].append(dest)
        
#         visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

#         def dfs(course):
#             if visited[course] == 1:
#                 return False  # cycle detected
#             if visited[course] == 2:
#                 return True   # already checked, no cycle
            
#             visited[course] = 1  # mark as visiting
#             for neighbor in graph[course]:
#                 if not dfs(neighbor):
#                     return False
#             visited[course] = 2  # mark as visited
#             return True

#         for course in range(numCourses):
#             if not dfs(course):
#                 return False
#         return True
