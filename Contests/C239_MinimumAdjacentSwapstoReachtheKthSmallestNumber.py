class Solution(object):
    #     def getNextBiggerNum(num):
    #         num_s = str(num)
    #         len_s = len(num_s)
    #         for i in range(len_s-2, -1, -1): # start from here, to right
    #             minRight = float('inf')
    #             minInd = -1
    #             for j in range(i+1, len_s): # find the num that's bearly bigger
    #                 if int(num_s[j]) <  minRight:
    #                     minRight = int(num_s[j])
    #                     minInd = j
    #             if minInd != -1: # swap i and j
    #                 return int(num_s[:])

    #         """
    #         1. if want to make a digit bigger, you're making another digit smaller
    #         2. so, if want to make the number bigger, can only try to find bigger number on the right hand side of it

    #         this is how we can GET the k-th smallest
    #         """
    #         for i in range(k):

    #         """
    #         how about count the number of neighbor swaps?

    #         use a graph algo
    #         """

    def getNextPermutation(self, s):
        def swapCharDirect(s, i, j):
            return s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]

        """
        - from right -> left, find the 1st element i s.t. num[i] < num[i+1]
            - now, we also know that num[i+1:] are desc-sorted
        - [really hard logic] quoted: "# Find the largest index j greater than i such that a[i] < a[j]"
            - it's like: a[i],a[i+1],a[i+2],...,a[j],...a[-1]
            - now a[i]<a[j] and j is largest, so a[i]>a[j+1]
            - so it's like sorted desc by: a[i+1],a[i+2],...,a[j],a[i],a[j+1],...,a[-1]
        - next permutation is like: a[j],a[-1],a[-2],...,a[j+1],a[i],a[j-1],...,a[i+2],a[i+1]
        """
        len_s = len(s)
        for i in range(len_s - 2, -1, -1):  # i=len_s-2, len_s-3, ..., 0
            if s[i] < s[i + 1]:  # found one
                for j in range(len_s - 1, i, -1):
                    if s[i] < s[j]:
                        s = swapCharDirect(s, i, j)
                        return s[:i + 1] + s[i + 1:][::-1]
        # if ind == -1:   # no need to consider per question condition

    def getMinSwaps(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: int
        """

        def swapCharNeighbor(s, i, j):  # different than swapCharDirect! side-effect...
            return s[:i] + s[j] + s[i:j] + s[j + 1:]

        def findCharToSwapAndCnt(s, sj):
            """
            always swap s[0] and closest (left->right) s[j] s.t. s[j]==sj
            """
            for j in range(1, len(s)):
                if s[j] == sj:
                    return swapCharNeighbor(s, 0, j), j

        num0 = num

        # get the kth biggest num
        for _ in range(k):
            num = self.getNextPermutation(num)

        # calc the number of swaps
        numSwaps = 0
        for i in range(len(num0)):
            if num0[i] != num[i]:
                newSubS, j = findCharToSwapAndCnt(num0[i:], num[i])
                num0 = num0[:i] + newSubS
                print(num0)
                numSwaps += j
        return numSwaps


