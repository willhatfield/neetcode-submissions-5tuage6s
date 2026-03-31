# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, pathMax = float('-inf')) -> int:
        if root is None:
            return 0

        if root.val >= pathMax:
            count = 1
        else:
            count = 0

        pathMax = max(pathMax, root.val)

        left = self.goodNodes(root.left, pathMax)
        right = self.goodNodes(root.right, pathMax)

        return count + left + right
