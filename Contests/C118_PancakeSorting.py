'''

Given an array A, we can perform a pancake flip: We choose some positive integer k <= A.length, then reverse the order of the first k elements of A.  We want to perform zero or more pancake flips (doing them one after another in succession) to sort the array A.

Return the k-values corresponding to a sequence of pancake flips that sort A.  Any valid answer that sorts the array within 10 * A.length flips will be judged as correct.



Example 1:

Input: [3,2,4,1]
Output: [4,2,4,3]
Explanation:
We perform 4 pancake flips, with k values 4, 2, 4, and 3.
Starting state: A = [3, 2, 4, 1]
After 1st flip (k=4): A = [1, 4, 2, 3]
After 2nd flip (k=2): A = [4, 1, 2, 3]
After 3rd flip (k=4): A = [3, 2, 1, 4]
After 4th flip (k=3): A = [1, 2, 3, 4], which is sorted.
Example 2:

Input: [1,2,3]
Output: []
Explanation: The input is already sorted, so there is no need to flip anything.
Note that other answers, such as [3, 3], would also be accepted.


Note:

1 <= A.length <= 100
A[i] is a permutation of [1, 2, ..., A.length]

'''


class Solution(object):
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        A_origin = A

        global_rec = []

        def find_maxInd(alist):
            max_ind, max_val = 0, alist[0]
            for i in range(1, len(alist)):
                if alist[i] > max_val:
                    max_ind, max_val = i, alist[i]
            return max_ind

        def sort_first_k(A, k):
            if k == 0:
                return
            if A == sorted(A):
                return

            max_ind = find_maxInd(A[:k])
            A = A[:max_ind + 1][::-1] + A[max_ind + 1:k] + A[k:]
            global_rec.append(max_ind + 1)
            A = A[:k][::-1] + A[k:]
            global_rec.append(k)

            sort_first_k(A, k - 1)

        sort_first_k(A, len(A))

        A = A_origin
        return global_rec