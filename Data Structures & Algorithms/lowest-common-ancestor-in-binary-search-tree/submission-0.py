class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == q or root == p:
            return root
        else:
            small, large = min(p.val, q.val), max(p.val, q.val)
            if small < root.val and root.val < large:
                return root
            elif small < root.val and large < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            elif small > root.val and large > root.val:
                return self.lowestCommonAncestor(root.right, p, q)
            return root