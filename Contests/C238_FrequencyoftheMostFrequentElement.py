class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l = 0
        r = 1
        slideSum = nums[0]
        maxFreq = 1
        for r in range(1, len(nums)):
            """ try pushing all elements to nums[r]"""

            """what can we easily do? slideSum
            this needs to hold: (r-l+1)*nums[r] - slideSum <= k
            """
            slideSum += nums[r]
            while (r - l + 1) * nums[r] - slideSum > k:
                slideSum -= nums[l]
                l += 1  # order cannot be wrong !
            maxFreq = max(maxFreq, r - l + 1)
        return maxFreq