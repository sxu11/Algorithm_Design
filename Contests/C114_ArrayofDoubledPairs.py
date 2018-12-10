class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        xaxis = [0] * 200001
        for a in A:
            xaxis[a + 100000] += 1

        num_1s = len(A)
        sorted_A = sorted(A)
        # i = 0
        # j = len(A)-1

        for a in sorted_A:
            if a > 0:
                break
            if xaxis[a + 100000] == 0:
                continue
            if a % 2 == 1:
                return False
            if xaxis[a / 2 + 100000] == 0:
                return False
            xaxis[a + 100000] -= 1
            xaxis[a / 2 + 100000] -= 1
            num_1s -= 2

        for a in sorted_A[::-1]:
            if a < 0:
                break
            if xaxis[a + 100000] == 0:
                continue
            if a % 2 == 1:
                return False
            if xaxis[a / 2 + 100000] == 0:
                return False
            xaxis[a + 100000] -= 1
            xaxis[a / 2 + 100000] -= 1
            num_1s -= 2

        return num_1s == 0
#         while sorted_A and sorted_A[0] <= 0:
#             if sorted_A[0]%2 != 0:
#                 return False
#             try:
#                 k = sorted_A.index(sorted_A[0]/2)
#             except:
#                 return False
#             sorted_A = sorted_A[1:k] + sorted_A[k+1:]

#         while sorted_A and sorted_A[-1] >= 0:
#             if sorted_A[-1]%2 != 0:
#                 return False
#             try:
#                 k = sorted_A.index(sorted_A[-1]/2)
#             except:
#                 return False
#             sorted_A = sorted_A[:k] + sorted_A[k+1:-1]
#         return len(sorted_A)==0
