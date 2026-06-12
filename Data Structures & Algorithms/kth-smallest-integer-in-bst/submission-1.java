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
    int ans;
    int times;
    public int kthSmallest(TreeNode root, int k) {
        times = k;
        dfs(root);
        return ans;
    }
    private void dfs(TreeNode root) {
        if (times == 0) return;
        if(root == null) return;
        dfs(root.left);
        times -= 1;
        if(times == 0) ans = root.val;
        dfs(root.right);
    }
}
