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
    int idx = 0;
    HashMap<Integer, Integer> pos = new HashMap<>();
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++) {
            pos.put(inorder[i], i);
        }
        return construct(preorder, 0, inorder.length - 1);

    }
    private TreeNode construct(int[] preorder, int left, int right) {
        if(left > right) return null;
        int val = preorder[idx];
        TreeNode cur = new TreeNode(val);
        idx += 1;
        cur.left = construct(preorder, left, pos.get(val)-1);
        cur.right = construct(preorder, pos.get(val)+1,right);
        return cur;
    }
}
