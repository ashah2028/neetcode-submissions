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
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> trav = new ArrayList<>();
        Queue<TreeNode> bfs = new LinkedList<>();

        bfs.add(root);

        while (!bfs.isEmpty()){
            List<Integer> level = new ArrayList<>();

            for (int i = bfs.size(); i > 0; i--){
                TreeNode node = bfs.poll();
                if (node != null){
                    level.add(node.val);
                    bfs.add(node.left);
                    bfs.add(node.right);

                }

            }

            if (level.size() > 0){
                trav.add(level);
            }
        }
        return trav;
    }
}
