class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        # --- 1. sieve to find primes ---
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False
        
        # --- 2. build graph ---
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * (n + 1)
        
        # --- 3. precompute non-prime component sizes ---
        comp_size = [0] * (n + 1)
        
        def dfs(u):
            stack = [u]
            nodes = []
            visited[u] = True
            
            while stack:
                x = stack.pop()
                nodes.append(x)
                for nei in graph[x]:
                    if not visited[nei] and not is_prime[nei]:
                        visited[nei] = True
                        stack.append(nei)
            
            size = len(nodes)
            for node in nodes:
                comp_size[node] = size
        
        # compute components for non-prime nodes
        for i in range(1, n+1):
            if not visited[i] and not is_prime[i]:
                dfs(i)
        
        res = 0
        
        # --- 4. process each prime node ---
        for p in range(1, n+1):
            if not is_prime[p]:
                continue
            
            seen = set()
            total = 0  # cumulative size
            
            for nei in graph[p]:
                if is_prime[nei]:
                    continue
                
                size = comp_size[nei]
                
                # avoid double counting same component
                if nei in seen:
                    continue
                
                seen.add(nei)
                
                # cross-component paths
                res += total * size
                
                # single-side paths
                res += size
                
                total += size
        
        return res