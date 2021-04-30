"""
Difference between reconstruct the tree #105 preorder/postorder + inorder and this problem which just uses preorder

#105 preorder/postorder + inorder: why we have to use 2 lists/traversals?
The lists does not preserve the null, so we do not have an indicator to check if a node is in the left subtree or right subtree, so 2 traversals are needed.
But for this problem, we can preserve null, so we can reconstruct by just using 1 list, i.e. preorder list.(Q: can we do it just using postorder or inorder? )
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from collections import deque
class Codec:
    def dfs(self, root, res):
        if not root:
            res.append("N")
        else:
            res.append(str(root.val))
            self.dfs(root.left, res)
            self.dfs(root.right, res)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        """
        res = []

        # how many lvls are there? 

        d = deque(root)
        while d:
            node += d.popleft()
            if node:
                res.append(str(node.val))  
                d.append(res.left)
                d.append(res.right)
            else:
                res.append("N")

        #for e.g.1:
        #1,2,3, , ,4,5

        return ",".join(res)
        """
        res = []
        self.dfs(root, res)
        # print("After serialization:", res)
        return ",".join(res)

    def dfsReverse(self, data):
        if data:
            if data[0] == "N":
                return None, data[1:]
            else:
                node = TreeNode(data[0])
                nodeLeft, dataRem = self.dfsReverse(data[1:])
                nodeRight, dataRem2 = self.dfsReverse(dataRem)
                node.left = nodeLeft
                node.right = nodeRight
                return node, dataRem2

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # self.constructRootWithList(data.split(','), root)
        node, _ = self.dfsReverse(data.split(","))
        # print("data.split:", data.split(","))
        return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))