# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = k
        arr = []
        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            self.cnt -= 1
            arr.append(node.val)
            if self.cnt == 0:
                return
            dfs(node.right)
        dfs(root)
        return arr[k - 1]