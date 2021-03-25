# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    # self.maxSum = 0

    def dfs(self, node, curSum, maxSum):
        """return the max, from node, to every descendents"""
        if node == None:
            return maxSum
        curSum += node.val
        maxSum = max([maxSum, curSum])

        leftMaxSum = self.dfs(node.left, curSum, maxSum)
        rightMaxSum = self.dfs(node.right, curSum, maxSum)
        return max([maxSum, leftMaxSum, rightMaxSum])

    def maxPathSum(self, root: TreeNode) -> int:
        """ maxPath possibly comes from:
        1. pass the root
            - left arm max + root.val + right arm max
            - right arm
                - how to find the paths, from the root, to every node on root.right?
                    - tool: dfs
                        - use a global curVal to record
                        - variation: when exit from a node, minus the global curVal
                    -
        2. left's max
        3. right's max
        """
        # if root == None: #
        """
        ok, this is wrong.. 
        think about when input=[-3]
        always double check empty cases
        might not correspond to 0"""
        # return 0

        if root.left != None:
            leftArmMax = self.dfs(root.left, 0, 0)
            leftMax = self.maxPathSum(root.left)
        else:
            leftArmMax = 0
            leftMax = -float("inf")
        if root.right != None:
            rightArmMax = self.dfs(root.right, 0, 0)
            rightMax = self.maxPathSum(root.right)
        else:
            rightArmMax = 0
            rightMax = -float("inf")
        return max([leftMax,
                    rightMax,
                    root.val + leftArmMax + rightArmMax
                    ])
