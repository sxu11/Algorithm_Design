'''

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.



Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Note:

1 <= N <= 9
0 <= K <= 9

'''


class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        # TODO if N==1, first digit i can be 0
        if N == 1:
            return range(10)

        class Tree:
            def __init__(self, val):
                # self.left = None
                # self.right = None
                self.val = val  #

        all_ress = []

        def dfs(node):
            if len(node.val) == N:
                all_ress.append(int(node.val))

            else:
                cur_tail = int(node.val[-1])
                if cur_tail - K >= 0:
                    dfs(Tree(node.val + str(cur_tail - K)))

                if K != 0 and cur_tail + K <= 9:  # K==0 is not expected..
                    dfs(Tree(node.val + str(cur_tail + K)))

        for i in range(1, 10):
            tree = Tree(str(i))
            dfs(tree)
        return all_ress
