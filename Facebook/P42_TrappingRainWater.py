class Solution:
    def trap(self, height: List[int]) -> int:
        """ at each i, its capability was determined by high[i]-low[i]
        - low[i] is itself
        - high[i] comes from:
          1. highest of its left side
          2. highest of its right side
          - lower of above

        How do we get high[i], defined as:
        - highest before [:i]
        """
        if not height:
            return 0

        leftHighs = [height[0]]
        curHighest = height[0]
        for i in range(1, len(height)):
            curHighest = max(curHighest, height[i])
            leftHighs.append(curHighest)

        rightHighs = [height[-1]]
        curHighest = height[-1]
        for i in range(len(height) - 2, -1, -1):
            curHighest = max(curHighest, height[i])
            rightHighs.append(curHighest)
        rightHighs = rightHighs[::-1]

        res = 0
        for i in range(len(height)):
            higher = min(leftHighs[i], rightHighs[i])
            res += max(0, higher - height[i])
        return res