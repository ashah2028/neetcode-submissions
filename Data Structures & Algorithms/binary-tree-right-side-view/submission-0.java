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
    public List<Integer> rightSideView(TreeNode root) {

        List<Integer> result = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();

        // bfs

        q.add(root);

        while (!q.isEmpty()){
            // need to add variable to get O(n) time complexity
            TreeNode right = null;
            for (int i = q.size(); i > 0; i--){
                TreeNode node = q.poll();
                if (node != null){
                    right = node;
                    q.add(node.left);
                    q.add(node.right);
                }
            }
            if (right != null){
                result.add(right.val);
            }
        }
        return result;
            


        
    }
}
