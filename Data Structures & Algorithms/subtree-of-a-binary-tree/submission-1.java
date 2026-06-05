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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (subRoot == null){
            // Root tree always has a null value
            return true; 
        }
        if (root == null){
            //If the root is null and subroot is not, no match
            return false;
        }
        if(isTreeSub(root, subRoot)){
            return true;
        }
        return isSubtree(root.left, subRoot) ||
         isSubtree(root.right, subRoot);

        

    }
    public boolean isTreeSub(TreeNode root, TreeNode subRoot){
        if (root == null && subRoot == null){
            return true;
        }
        if (root != null && subRoot != null && root.val == subRoot.val){
            return isTreeSub(root.left, subRoot.left) && 
            isTreeSub(root.right, subRoot.right);
        }
        return false;
    }


}
