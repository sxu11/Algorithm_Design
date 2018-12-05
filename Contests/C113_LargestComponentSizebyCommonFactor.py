'''
Still TLE...
'''


class Solution:
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # num2primes = {}
        prime2inds = {}
        ind2cnt = {}

        parents = range(len(A))

        def find(i):
            if parents[i] != i:
                return find(parents[i])
            else:
                return i

        cnts = [1] * len(A)

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parents[root_i] = root_j  # This step!! not on i,j any more...
                cnts[root_j] += cnts[root_i]  # This step!! not on i,j any more...

        prime2nums = {}
        for i in range(len(A)):
            a = A[i]
            # cur_primes = []

            for k in range(2, A[i] + 1):  # TODO: itself!!!
                if a % k == 0:
                    # cur_primes.append(k)

                    if k in prime2inds:
                        prime2inds[k].append(i)
                        # prime2nums[k].append(A[i])
                    else:
                        prime2inds[k] = [i]
                        # prime2nums[k] = [A[i]]

                    a /= k
                    while a % k == 0:
                        a /= k
            # num2primes[a_origin] = cur_primes

        '''
        Union step
        '''
        for inds in prime2inds.values():
            i = inds[0]
            for j in inds[1:]:
                union(i, j)

        return max(cnts)
