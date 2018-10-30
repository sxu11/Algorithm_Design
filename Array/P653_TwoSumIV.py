
'''

Thought will be boring to pre-order, and print, and use dict. O(n) time + O(n) space.

Actual difference:
Again (after TwoSumIII), no need to return the inds. so dict --> set.

According to Python wiki: Time complexity, set is implemented as a hash table.
So you can expect to lookup/insert/delete in O(1) average. Unless your hash
table's load factor is too high, then you face collisions and O(n).

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorder(self, root, k, a_set):
        if root:
            if root.val in a_set:
                return True
            else:
                a_set.add(k - root.val)
                return self.preorder(root.left, k, a_set) or self.preorder(root.right, k, a_set)
        return False

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        a_set = set()
        return self.preorder(root, k, a_set)