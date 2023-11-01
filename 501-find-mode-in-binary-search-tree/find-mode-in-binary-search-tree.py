# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    prev = None
    result = []
    current = 0
    maxi = 0

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.dfs(root)
        return self.result
    
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        if root.val == self.prev:
            self.current += 1
        else:
            self.current = 1
        
        if self.current == self.maxi:
            self.result.append(root.val)
        elif self.current > self.maxi:
            self.result = [root.val]
            self.maxi = self.current

        self.prev = root.val
        self.dfs(root.right)