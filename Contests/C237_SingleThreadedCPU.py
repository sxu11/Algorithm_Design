import heapq


class Solution:

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """[[1,2],[2,4],[3,2],[4,1]]
        taskNum = 4
        """

        q = []
        taskNum = len(tasks)
        tasks_indexed = [(tasks[i][1], i, tasks[i][0]) for i in range(taskNum)]
        # period, ind, startTime
        tasks_sorted = sorted(tasks_indexed, key=lambda task: (task[2], task[0]))
        res = [tasks_sorted[0][1]]
        t = tasks_sorted[0][0] + tasks_sorted[0][2]

        i = 1
        while len(res) < taskNum:  # i < taskNum:
            for j in range(i, taskNum):
                if tasks_sorted[j][2] <= t:
                    # print("yes")
                    heapq.heappush(q, tasks_sorted[j])
                    i = j + 1
                else:
                    i = j
                    break

            if not q:
                # break
                heapq.heappush(q, tasks_sorted[i])
                i += 1
                # t += tasks_sorted[i][0]

            task = heapq.heappop(q)

            t += task[0]
            res.append(task[1])

        return res

        """
    def __init__(self):
        self.done = []

    def getMinTime(self, remain_tasks):
        minTime = float("inf")
        for i in range(0, len(remain_tasks)):
            if not self.done[i] and remain_tasks[i][0] < minTime:
                minTime =  remain_tasks[i][0]
        return minTime

    def getShortestTask(self, remain_tasks, t):
        ind = -1
        shortTaskTime = float("inf")
        for i in range(0, len(remain_tasks)):
            if not self.done[i] and remain_tasks[i][0] <= t and remain_tasks[i][1] < shortTaskTime:
                shortTaskTime = remain_tasks[i][1]
                ind = i
        return ind

    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        t = 0
        res = []
        remain_tasks = tasks
        remain_cnt = len(remain_tasks)
        self.done = [False] * remain_cnt
        t = self.getMinTime(remain_tasks)
        while remain_cnt > 0:
            i = self.getShortestTask(remain_tasks, t)
            self.done[i] = True
            t += remain_tasks[i][1]
            # remain_tasks = remain_tasks[:i] + remain_tasks[i+1:]
            remain_cnt -= 1
            res.append(i)
        return res
        """
