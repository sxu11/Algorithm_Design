
'''
Given a list of non-negative numbers and a target integer k,
write a function to check if the array has a continuous subarray
of size at least 2 that sums up to the multiple of k, that is,
sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''

'''
There is even a math thinking behind this: 
Compute the mod of the sum(nums[:i]) as the i's element. 
If mod repeats, then there is a solution... 

Essence: The unit of computing is nums[:i], not nums[j:i]!!!

W/o math, use a set record all mods of nums[j:i] for j<=i,
and how this set is updated. 
Not the best point of view to tackle this problem. 
So a looooot of corner cases to consider. 
'''

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        '''
        Corner case 1: k = 0
        '''
        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] == 0:
                    return True
            return False

        '''
        Corner case 2: k not 0, but two consecutive 0's (always eligible)
        '''
        for i in range(len(nums) - 1):
            if nums[i] == 0 and nums[i + 1] == 0:
                return True

        '''
        Corner case 3: k is negative
        '''
        k = abs(k)

        my_set = set()
        for i in range(len(nums)):
            if k - (nums[i] % k) in my_set:
                return True

            else:
                new_set = set([nums[i]])
                for val in my_set:
                    new_set.add((val + nums[i]) % k)
                my_set = new_set
        return False