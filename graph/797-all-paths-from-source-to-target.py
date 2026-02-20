class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Idea: DFS to explore all paths from node 0 to node n-1
        # Graph is a DAG (no cycles), so we can explore without visited set
        
        n = len(graph)
        target = n - 1
        result = []
        
        def dfs(node, path):
            # Base case: reached target node
            if node == target:
                result.append(path[:])  # Add copy of current path
                return
            
            # Explore all neighbors
            for neighbor in graph[node]:
                path.append(neighbor)      # Add neighbor to path
                dfs(neighbor, path)        # Recurse
                path.pop()                 # Backtrack
        
        # Start DFS from node 0
        dfs(0, [0])
        
        return result