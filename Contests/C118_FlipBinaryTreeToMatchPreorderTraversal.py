# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """

        # when to len diff?
        self.ind = 0

        all_nodes_flipped = []

        if root.val != voyage[self.ind]:
            return [-1]

        def flip(node):
            node.left, node.right = node.right, node.left
            all_nodes_flipped.append(node.val)
            return node

        def check_subtree(node):
            # if ind >= len(voyage):
            # return True
            # if ind==len(voyage)-1 and (not node.left or voyage[ind]!=node.left.val) and (not node.right or voyage[ind]!=node.right.val):
            #    return False

            # if node.left and node.left.val == voyage[ind]:
            #    pass
            # elif node.left and node.right and node.right.val == voyage[ind]:
            #    node = flip(node)
            # elif (not node.left) and node.right and node.right.val == voyage[ind]:
            #    # print 'there!'
            #    pass
            # elif (node.left is None) and (node.right is None):
            #    return True
            # elif node.left and node.left.val!=voyage[ind] and node.right and node.right.val!=voyage[ind]:
            #    return False
            # else:
            # print node.val, voyage[ind] #node.left, node.right, ind, len(voyage)-1
            # print 'here!'
            #    pass
            if node.val != voyage[self.ind]:
                return False

            self.ind += 1

            if (not node.left) and (not node.right):
                return True

            elif (not node.right):
                if node.left.val != voyage[self.ind]:
                    # print node.left.val, voyage[self.ind]
                    return False
                else:
                    return check_subtree(node.left)

            elif (not node.left):
                if node.right.val != voyage[self.ind]:
                    return False
                else:
                    return check_subtree(node.right)

            else:
                if node.left.val == voyage[self.ind]:
                    return check_subtree(node.left) and check_subtree(node.right)
                elif node.right.val == voyage[self.ind]:
                    node = flip(node)
                    return check_subtree(node.left) and check_subtree(node.right)
                else:
                    return False

            # is_success = True
            # if node.left:
            #     is_success = check_subtree(node.left)
            # if node.right:
            #     is_success = check_subtree(node.right) and is_success
            # return is_success

        is_success = check_subtree(root)
        if not is_success:
            return [-1]
        else:
            return all_nodes_flipped


