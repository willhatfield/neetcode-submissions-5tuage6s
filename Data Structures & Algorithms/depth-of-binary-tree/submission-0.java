/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int maxDepth(TreeNode root) {
        return maxDepthHelper(root, 0);
    }

    public int maxDepthHelper(TreeNode root, int h) {
        if(root == null)    {
            return h;
        }

        int l = maxDepthHelper(root.left, h + 1);
        int r = maxDepthHelper(root.right, h + 1);

        return Math.max(l, r);
    }
}
