class Solution:
    def constructLeftBnds(self, nums):
        """for i, it's last left j s.t. nums[j] >= nums[i]"""
        leftBnds, st = []  #
        for i in range(len(nums)):
            while st and nums[st[-1]] >= nums[i]:
                j = st.pop()
            if not st:
                leftBnds.append(0)
            else:
                leftBnds.append(st[-1] + 1)  # not j here!!!
                """st[-1]+1 != j, where is the gap?
                - this is a fact, because previous can pop out. 
                Then which one should we choose j? can we make sure nums[j] >= nums[i]
                yes, since we put i into st as a test bnd. "greedy". 
                so if i+1 can pass i, it can always pass whatever was passed by i already..."""
            st.append(i)
        return leftBnds

    def maxSumMinProduct(self, nums: List[int]) -> int:
        mode = 10 ** 9 + 7
        numLen = len(nums)
        leftBnds = self.constructLeftBnds(nums)
        rightBnds = self.constructLeftBnds(nums[::-1])
        rightBnds = [numLen - 1 - x for x in rightBnds[::-1]]
        preSums = []  # this should be of len:(n+1)!!!
        curPreSum = 0
        """define: preSums[i] as (inclusive) the sum of num[0],num[1],...,num[i]
        when i=0, it's num[0]
        when i=n-1, it's num[0],num[1],...,num[n-1]"""
        for i in range(len(nums)):
            curPreSum += nums[i]
            preSums.append(curPreSum)
        res = 0
        for i in range(len(nums)):
            # curRes = sum(nums[leftBnds[i]:rightBnds[i]+1]) * nums[i]
            if leftBnds[i] > 0:
                curRes = (preSums[rightBnds[i]] - preSums[leftBnds[i] - 1]) * nums[i]
            else:
                curRes = preSums[rightBnds[i]] * nums[i]
            # needs sum of inds: leftBnds[i], leftBnds[i]+1, leftBnds[i]+2, ..., rightBnds[i]
            # which is equal to (0,1,2,...,rightBnds[i]) - (0,1,2,...,leftBnds[i]-1)
            res = max(res, curRes)
        return res % mode

