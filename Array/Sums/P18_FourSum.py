

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # TODO: check best solution

        def find_all_combs(alist, atarget):
            combs = []
            i = 0
            j = len(alist) - 1
            while i < j:
                if alist[i] + alist[j] == atarget:
                    combs.append([alist[i], alist[j]])
                    i += 1  # TODO
                    j -= 1
                    while i < j and alist[i] == alist[i - 1]:  # TODO: while i<j and alist[i]==alist[i+1]
                        i += 1
                    while i < j and alist[j] == alist[j + 1]:  # while i<j and alist[j]==alist[j-1]
                        j -= 1
                elif alist[i] + alist[j] > atarget:
                    j -= 1
                else:
                    i += 1

            return combs

        all_combs = []
        nums_sorted = sorted(nums[:])
        for i in range(len(nums_sorted) - 3):
            for j in range(i + 1, len(nums_sorted) - 2):
                curr_subscombs = find_all_combs(nums_sorted[j + 1:], target - nums_sorted[i] - nums_sorted[j])
                curr_subscombs = [[nums_sorted[i], nums_sorted[j]] + x for x in curr_subscombs]
                all_combs += curr_subscombs

        # deduplicate
        new_all_combs = []
        for x in all_combs:
            if x not in new_all_combs:
                new_all_combs.append(x)
        return list(new_all_combs)