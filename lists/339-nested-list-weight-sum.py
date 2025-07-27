class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested, depth):
            total = 0
            for item in nested:
                if item.isInteger():
                    total += depth * item.getInteger()
                else:
                    total += dfs(item.getList(), depth + 1)
            return total
        return dfs(nestedList, 1)
