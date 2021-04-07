# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        Inorder (Left, Root, Right)
        Preorder (Root, Left, Right)
        Postorder (Left, Right, Root)

        1. Last element of postorder: root
        2. Find in inorder: split left and right
        Construct left and right recursively

        this function takes
            - inorder
            - postorder
        return the root
        """
        if len(postorder) == 0:
            return None

        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        for i in range(len(inorder)):
            if rootVal == inorder[i]:
                root.left = self.buildTree(inorder[:i], postorder[:i])
                root.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        return root


