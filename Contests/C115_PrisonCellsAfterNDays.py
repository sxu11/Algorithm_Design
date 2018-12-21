class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """

        '''
        Brutal force: direct simulate
        '''

        def iter_1_step(cur_state):
            next_state = [0] * 8

            for j in range(1, 7):
                if cur_state[j - 1] == cur_state[j + 1]:
                    next_state[j] = 1
            cur_state = next_state
            return cur_state

        cur_state = cells[:]
        state_inds = {}

        max_iter = 100000
        max_num_iters, num_iters_left = N / max_iter, N % max_iter

        if N < max_iter:
            for i in range(N):
                cur_state = iter_1_step(cur_state)
            return cur_state

        for ind in range(max_num_iters):
            for i in range(max_iter):
                cur_state_tuple = tuple(cur_state)
                if cur_state_tuple in state_inds:
                    '''
                    predict forward, stop right before N
                    '''
                    ind_pre, i_pre = state_inds[cur_state_tuple]
                    period_len = (ind - ind_pre) * max_iter + (i - i_pre)

                    left_len = N - ind * max_iter - i
                    remain_iters = left_len % period_len

                    for j in range(remain_iters):
                        cur_state = iter_1_step(cur_state)
                    return cur_state

                else:
                    state_inds[cur_state_tuple] = (ind, i)

                cur_state = iter_1_step(cur_state)

        return cur_state