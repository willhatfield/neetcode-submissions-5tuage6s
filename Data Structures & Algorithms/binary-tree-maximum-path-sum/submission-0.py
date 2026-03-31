# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode], currSum=0) -> int:
        self.best = -1001
        
        def dfs(root):
            if not root:
                return 0
            
            left_gain = max(0, dfs(root.left))
            right_gain = max(0, dfs(root.right))

            curr_path = root.val + left_gain + right_gain
            self.best = max(self.best, curr_path)

            return root.val + max(left_gain, right_gain)

        dfs(root)
        return self.best

