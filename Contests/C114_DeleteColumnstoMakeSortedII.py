class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        row, col = len(A), len(A[0])

        need_worry = [True] * row
        num_need_worry = row
        '''
        i need worry means A[i][prev_j] == A[i+1][prev_j] for all prev_j
        '''

        min_del_size = 0

        for j in range(col):
            cur_no_need_worry = []
            need_remove_col = False
            for i in range(row - 1):
                if not need_worry[i]:
                    continue

                if A[i][j] > A[i + 1][j]:
                    min_del_size += 1
                    need_remove_col = True
                    break
                elif A[i][j] < A[i + 1][j]:
                    cur_no_need_worry.append(i)

            if not need_remove_col:
                for i in cur_no_need_worry:
                    need_worry[i] = False
                    num_need_worry -= 1

                if num_need_worry == 0:
                    break
        return min_del_size

#         if A == sorted(A):
#             return 0

#         def inds_to_delete(Asub, k): # Asub rows
#             if len(Asub) == 0 or len(Asub) == 1 or k >= len(Asub[0]):
#                 return []

#             cur_col = [a[k] for a in Asub]
#             if cur_col != sorted(cur_col):
#                 return [k] + inds_to_delete(Asub, k+1)
#             else:
#                 groups = []
#                 is_new_group = True
#                 for i in range(len(cur_col)-1):
#                     if cur_col[i] == cur_col[i+1]:
#                         if is_new_group:
#                             new_group = [i,i+1]
#                             is_new_group = False
#                         else:
#                             new_group.append(i+1)
#                     else:
#                         if not is_new_group:
#                             groups.append(new_group[:])
#                             is_new_group = True
#                 if not is_new_group:
#                     groups.append(new_group[:])
#                     is_new_group = True

#                 all_inds = []
#                 for group in groups:
#                     Asub = [A[i] for i in group]
#                     cur_inds = inds_to_delete(Asub, k+1)
#                     all_inds += cur_inds[:]
#                 return all_inds

#         print inds_to_delete(A, 0)
#         return len(list(set(inds_to_delete(A, 0))))

#         min_del = 0
#         for j in range(0,strlen):
#             # j is the col to look at
#             cur_col = [a[j] for a in A]

#             if cur_col != sorted(cur_col):
#                 min_del += 1
#                 continue
#             else:
#                 # sorted, only need to worry about equal subsets
#                 # grouping i's into subgroups
#                 groups = []


# min_del += 1


#             A_trimmed = [word[j:] for word in A]


#             if A_trimmed == sorted(A_trimmed):
#                 return min_del