# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #Binary Tree so will have to explore both directions 
        #Keep track of the max value in each recursion to determine if add to counter
        counter = 0
        def dfs(node, val):
            nonlocal counter
            if not node: 
                return 
            elif node.val >= val:
                counter += 1
                dfs(node.left, node.val)
                dfs(node.right, node.val)
            else:
                dfs(node.left, val)
                dfs(node.right, val)
        dfs(root, root.val)
        return counter

