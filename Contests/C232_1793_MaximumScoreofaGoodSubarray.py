class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        left = k
        right = k
        maxScore = nums[k]
        curMin = nums[k]
        while left >= 0 or right < len(nums):
            """can still proceed even if either reached end"""
            if right == len(nums) - 1 and left == 0:
                break

            #           Following is so wrong!! Don't mix 2-layer logic into an "or", plz!
            #
            # elif (right == len(nums)-1) or (nums[left-1] > nums[right+1]):
            #     left -= 1
            #     curMin = min(curMin, nums[left])
            # else:
            #     right += 1
            #     curMin = min(curMin, nums[right])
            #

            elif left > 0 and right < len(nums) - 1:
                if nums[left - 1] > nums[right + 1]:
                    left -= 1
                    curMin = min(curMin, nums[left])
                else:
                    right += 1
                    curMin = min(curMin, nums[right])

            elif right == len(nums) - 1:
                left -= 1
                curMin = min(curMin, nums[left])
            else:
                right += 1
                curMin = min(curMin, nums[right])

            maxScore = max(maxScore, curMin * (right - left + 1))
        return maxScore