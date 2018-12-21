# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        queue = [root]
        while len(queue) > 0:
            cur_node = queue[0]
            if cur_node is None:
                for node in queue[1:]:
                    if node is not None:
                        return False
                break

            queue = queue[1:] + [cur_node.left, cur_node.right]
        return True
