
from collections import Counter

'''
Stephan's solution
'''
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        AB = Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)


'''
Mine
'''
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        from collections import Counter
        D_cnt = Counter(D)
        cnt = 0
        for i in range(len(A)):
            for j in range(len(B)):
                for k in range(len(C)):
                    if -(A[i]+B[j]+C[k]) in D_cnt:
                        cnt += D_cnt[-(A[i]+B[j]+C[k])]
        return cnt