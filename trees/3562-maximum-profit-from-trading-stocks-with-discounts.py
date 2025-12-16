class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], 
                  hierarchy: List[List[int]], budget: int) -> int:
        """
        Tree DP solution for maximizing profit with parent-child discount rules.
        
        Key idea: When a parent stock is bought, children get 50% discount.
        We need to track two states for each node:
        - dp0: best profit when this node is bought at FULL price (no parent discount)
        - dp1: best profit when this node is bought at DISCOUNTED price (parent bought it)
        """
        
        # Build adjacency list for the tree
        children = [[] for _ in range(n)]
        for edge in hierarchy:
            u, v = edge
            u_idx = u - 1  # Convert to 0-indexed
            v_idx = v - 1
            children[u_idx].append(v_idx)
        
        # Use negative infinity to mark invalid/unreachable states
        INF = -10**9
        
        # These will be populated by DFS (not actually used, could be removed)
        dp0_list = [None] * n
        dp1_list = [None] * n
        
        def dfs(u):
            """
            Compute DP for subtree rooted at u.
            
            Returns:
                dp0_u[b]: max profit using budget b, where u is bought at FULL price
                          (or not bought at all, if not buying u gives better profit)
                dp1_u[b]: max profit using budget b, where u is bought at DISCOUNT
                          (or not bought at all)
            """
            
            # base0[b]: max profit from children when u will be bought at full price
            #           Children must pay full price (no discount available)
            # base1[b]: max profit from children when u will be bought at discount
            #           Children can get discounts (because u is bought)
            base0 = [INF] * (budget + 1)
            base0[0] = 0  # No budget used, no profit
            
            base1 = [INF] * (budget + 1)
            base1[0] = 0  # No budget used, no profit
            
            # Process each child and merge their results
            for v in children[u]:
                dp0_v, dp1_v = dfs(v)
                
                # === Merge child v into base0 (u bought at full price) ===
                # When u is bought at full price, children pay FULL price
                # So we use dp0_v (child v bought at full price or not bought)
                new_base0 = [INF] * (budget + 1)
                for j in range(budget + 1):
                    if base0[j] == INF:
                        continue  # Skip invalid states
                    
                    # Try allocating k budget to child v
                    for k in range(0, budget - j + 1):
                        if j + k <= budget and dp0_v[k] != INF:
                            # j budget already used by previous children
                            # k budget used by child v
                            # Total: j + k
                            if new_base0[j + k] < base0[j] + dp0_v[k]:
                                new_base0[j + k] = base0[j] + dp0_v[k]
                
                base0 = new_base0
                
                # === Merge child v into base1 (u bought at discount) ===
                # When u is bought (whether full or discount), children get DISCOUNT
                # So we use dp1_v (child v bought at discount or not bought)
                new_base1 = [INF] * (budget + 1)
                for j in range(budget + 1):
                    if base1[j] == INF:
                        continue
                    
                    for k in range(0, budget - j + 1):
                        if j + k <= budget and dp1_v[k] != INF:
                            if new_base1[j + k] < base1[j] + dp1_v[k]:
                                new_base1[j + k] = base1[j] + dp1_v[k]
                
                base1 = new_base1
            
            # Now compute dp0_u and dp1_u by deciding whether to buy node u itself
            
            # === Compute dp0_u: node u bought at FULL price ===
            dp0_u = [INF] * (budget + 1)
            
            for b in range(budget + 1):
                # Option 1: Don't buy node u at all
                # Just use the profit from children (with no discount for them)
                if base0[b] != INF:
                    dp0_u[b] = base0[b]
                
                # Option 2: Buy node u at full price
                cost0 = present[u]
                if b >= cost0 and base1[b - cost0] != INF:
                    # Spend cost0 on buying u, leaving (b - cost0) for children
                    # Children get discount, so use base1[b - cost0]
                    # Profit from u = future[u] - cost0 (selling price - buying price)
                    profit = base1[b - cost0] + (future[u] - cost0)
                    if profit > dp0_u[b]:
                        dp0_u[b] = profit
            
            # === Compute dp1_u: node u bought at DISCOUNTED price ===
            dp1_u = [INF] * (budget + 1)
            
            for b in range(budget + 1):
                # Option 1: Don't buy node u at all
                # Just use the profit from children (with no discount for them)
                if base0[b] != INF:
                    dp1_u[b] = base0[b]
                
                # Option 2: Buy node u at discounted price (50% off)
                cost1 = present[u] // 2
                if b >= cost1 and base1[b - cost1] != INF:
                    # Spend cost1 (discounted) on buying u
                    # Children get discount, so use base1[b - cost1]
                    # Profit from u = future[u] - cost1 (HIGHER profit due to discount!)
                    profit = base1[b - cost1] + (future[u] - cost1)
                    if profit > dp1_u[b]:
                        dp1_u[b] = profit
            
            return dp0_u, dp1_u
        
        # Start DFS from root (node 0)
        # Root can only be bought at full price (no parent to give discount)
        dp0_root, _ = dfs(0)
        
        # Return maximum profit across all possible budgets
        return max(dp0_root)