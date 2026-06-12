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

public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        dfsSerialize(root, sb);
        return sb.toString();
    }
    private void dfsSerialize(TreeNode root, StringBuilder sb) {
        if(root == null){
            sb.append("#,");
            return;
        }
        sb.append(root.val);
        sb.append(',');
        dfsSerialize(root.left, sb);
        dfsSerialize(root.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        String[] arr = data.split(",");
        int[] idx = new int[1];

        return build(arr, idx);
    }

    private TreeNode build(String[] arr, int[] idx) {
        if(arr[idx[0]].equals("#")) {
            idx[0]++;
            return null;
        }
        TreeNode cur = new TreeNode(Integer.parseInt(arr[idx[0]]));
        idx[0]++;
        cur.left = build(arr, idx);
        cur.right = build(arr, idx);
        return cur;
    }
}
