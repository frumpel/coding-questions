# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def walkTree(self, node, val):
        if node == None:
            return True
        if node.val != val:
            return False
        return self.walkTree(node.left,val) and self.walkTree(node.right,val)

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        val=root.val
        return self.walkTree(root,val)
