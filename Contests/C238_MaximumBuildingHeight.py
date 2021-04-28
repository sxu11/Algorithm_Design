class Solution:
    """
    def applyLeftLimit(self, restrictions, n):
        # space by space, Okay, but slow

        if restrictions[0][0] == 1:
            curLimit = restrictions[0][1]
        else:
            curLimit = 9999999
        res = [curLimit]
        curInd = 1
        restriction_num = len(restrictions)
        for i in range(2,n+1):
            nextLimit = curLimit + 1
            if curInd < restriction_num and restrictions[curInd][0] == i:
                if restrictions[curInd][1] < nextLimit:
                    nextLimit = restrictions[curInd][1] # min(nextLimit, restrictions[curInd][1])
                curInd += 1
            res.append(nextLimit)
            curLimit = nextLimit
        return res

    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n-1
        restrictions = [[1,0]] + sorted(restrictions, key=lambda x:x[0])
        restrictions_reversed = [[n+1-x[0],x[1]] for x in restrictions[::-1]]
        # print(restrictions)
        # print(restrictions_reversed)

        leftLimit = self.applyLeftLimit(restrictions, n)
        rightLimit = self.applyLeftLimit(restrictions_reversed, n)[::-1]
        bothLimit = [min(leftLimit[i],rightLimit[i]) for i in range(n)]
        # print(leftLimit)
        # print(rightLimit)
        return max(bothLimit)
        """

    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        A = [[1, 0]] + sorted(restrictions, key=lambda x: x[0])
        m = len(A)

        if m == 1:
            return n - 1
        """
        1st, consider max heights at the restrictions

        left -> right:
        - i only limit i+1
        """
        for i in range(m - 1):
            A[i + 1][1] = min(A[i + 1][1], A[i][1] + A[i + 1][0] - A[i][0])

        """ right -> left """
        for i in range(m - 1, 0, -1):
            A[i - 1][1] = min(A[i - 1][1], A[i][1] + A[i][0] - A[i - 1][0])

        """
        2nd, extend the maximal restrictions to other places (x,y)
        if (and only if) both max A[i] and A[i+1] are fixed, then x,y satisfy:
        1. x-A[i][0] = y-A[i][1]
        2. A[i+1][0]-x = y-A[i+1][1]
        so 2y = A[i+1][0]-A[i][0]+A[i][1]+A[i+1][1]
        """
        maxRes = n - A[-1][0] + A[-1][1]  # 0 # 0???
        for i in range(m - 1):
            innerMax = (A[i + 1][0] - A[i][0] + A[i][1] + A[i + 1][1]) // 2
            maxRes = max(maxRes, innerMax)
        return maxRes