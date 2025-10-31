class Solution:
    def simplifyPath(self, path: str) -> str:
        """
        Simplify a Unix-style absolute path.
        
        Rules:
        - Single period '.' refers to current directory (ignore)
        - Double period '..' refers to parent directory (go up one level)
        - Multiple consecutive slashes are treated as a single slash
        - Path must start with '/' and not end with '/' (unless root)
        
        Approach: Use a stack to track directory names
        - Split path by '/' to get components
        - For each component:
          - If it's '..', pop from stack (if not empty)
          - If it's '.', empty string, or whitespace, ignore it
          - Otherwise, push to stack
        - Join stack with '/' and prepend '/'
        
        Time: O(n) where n is length of path
        Space: O(n) for the stack
        """
        stack = []
        
        # Split by '/' and process each component
        components = path.split('/')
        
        for component in components:
            if component == '..':
                # Go to parent directory (pop if possible)
                if stack:
                    stack.pop()
            elif component and component != '.':
                # Valid directory name (not empty, not '.')
                stack.append(component)
            # Ignore empty strings (from consecutive slashes) and '.'
        
        # Build simplified path
        return '/' + '/'.join(stack)

