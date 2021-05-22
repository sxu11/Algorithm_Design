import math


class Solution:
    #     def __init__(self):
    #         self.cache = dict()
    #         self.constructed = False
    #     def constructCache(self, n):
    #         mod = 10**9 + 7
    #         self.cache[(1,1)] = 1
    #         for i in range(1,n+1):
    #             for j in range(i,n+1):
    #                 if j==i:
    #                     self.cache[(i,j)] = i
    #                 else:
    #                     self.cache[(i,j)] = self.cache[(i,j-1)] * j
    #                     if self.cache[(i,j)] > mod:
    #                         self.cache[(i,j)] = self.cache[(i,j)] % mod
    #         # print(self.cache)
    @functools.lru_cache(None)
    def factorial(self, m, start=1):
        mod = 10 ** 9 + 7
        # res = 1
        # for i in range(start,m+1):
        #     res = (i*res) % mod
        # # self.cache[m] = res
        # return res #self.cache[m]
        if m < start:
            return 1
        elif m == start:
            return start
        else:
            return self.factorial(m - 1, start) * m
        # """ also use recursive on this one, with memory"""
        # if start>m: return 1
        # return self.cache[(start,m)]

    @functools.lru_cache(None)
    def rearrangeSticks(self, n: int, k: int) -> int:
        """ a total of n! arrangements
        - k = n: all visiable 1,2,3,4,5
        - k = n-1=4, only 1 invisible
            move 1: 2,3,4,5,1  2,1,3,4,5 ... (4 comb)
            move 2: 1,3,2,4,5  1,3,4,2,5 (3 comb)
            move 3: 2 comb      move 4: 1 comb
        - k = n-2=3: only 2 invisible, move 1,2: 3,[1,2],4,5
        def: from a segment of len n, get exact k visible
        return combinations """
        mod = 10 ** 9 + 7
        # if not self.constructed:
        # self.constructCache(n)
        # self.constructed = True
        if k == 1:  # n, set(1,2,3,...,n-1)
            return self.factorial(n - 1)
        # elif k == 2: # set(...) of size m with k=1, n, others of size n-m-1
        else:
            res = 0
            for m in range(k - 1, n):  # range(n-1,k-2,-1): #range(k-1,n): # left side number
                # m sticks on the left side, at most m visible
                # if k-1 > m, impossible; k-1 must <=m
                leftRes = self.rearrangeSticks(m, k - 1)
                # rightRes = (factorial(n-m-1) * math.comb(n-1,n-m-1)) % mod
                # forgot the combinations in the 1st try!!!
                # C_{n-m-1}^{n-1} = (n-1)! / (n-m-1)! m!, rightRes = (n-1)! / m!
                rightRes = self.factorial(n - 1, m + 1)  # int(self.factorial(n-1) / self.factorial(m))
                """ sequence of call:
                - last call: n-1 * n-2 * ... * m+2 * m+1
                - 2nd last: use n-1 to replace n, use k-1 to replace ... too hard to track """
                """ proactively reconstruct cache: goal is to do (n-1)! / m! 
                = n-1 * n-2 * ... * m+2 * m+1 where n and m both vary """
                res += (leftRes * rightRes) % mod
            return res % mod
