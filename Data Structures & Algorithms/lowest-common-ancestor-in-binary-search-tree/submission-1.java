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
    TreeNode ans;
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        lca(root, p, q);
        return ans;
    }

    private boolean lca(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null) return false;
        boolean left = lca(root.left, p, q);
        boolean right = lca(root.right, p, q);
        if ((left == true && right == true) || ((root.val == p.val || root.val == q.val) && (left || right))) {
            ans = root;
        }
        return (left || right || root.val == p.val || root.val == q.val);
    }
}
