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
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Integer.MAX_VALUE, Integer.MIN_VALUE);
    }
    private boolean dfs(TreeNode root, int mx, int mi) {
        if(root == null) return true;
        if(root.val >= mx || root.val <= mi) return false;
        boolean left = dfs(root.left, root.val, mi);
        boolean right = dfs(root.right, mx, root.val);
        if(left == false || right == false) return false;
        return true;
    }
}
