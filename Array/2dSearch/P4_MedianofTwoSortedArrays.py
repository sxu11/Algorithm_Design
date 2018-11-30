class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)

        if n == 0:
            if m % 2 == 0:
                return (nums1[m / 2] + nums1[m / 2 - 1]) / 2.
            else:
                return nums1[m / 2]
        if m == 0:
            if n % 2 == 0:
                return (nums2[n / 2] + nums2[n / 2 - 1]) / 2.
            else:
                return nums2[n / 2]

        '''
        the cnt of left nums is (m+n+1)/2
        '''
        i_min, i_max = 0, m - 1
        while True:
            i = (i_min + i_max) / 2  # mid, or right-to-mid
            j = (m + n + 1) / 2 - (i + 1) - 1
            #
            if j < -1 or (j<n-1 and i >=0 and nums1[i] > nums2[j + 1]):
                '''
                j is too small. i too big. 
                '''
                i_max = i - 1
            elif j >= n or (i<m-1 and j>=0 and nums2[j] > nums1[i + 1]):
                '''
                i is too small. j too big. 
                '''
                i_min = i + 1
            else:
                if j == n - 1:
                    min_of_right = nums1[i + 1]
                elif i == m - 1:
                    min_of_right = nums2[j + 1]
                else:
                    min_of_right = min(nums1[i + 1], nums2[j + 1])

                if j == -1:
                    max_of_left = nums1[i]
                elif i == -1:
                    max_of_left = nums2[j]
                else:
                    max_of_left = max(nums1[i], nums2[j])

                if (m + n) % 2 == 0:
                    return (max_of_left + min_of_right) / 2.
                else:
                    return max_of_left