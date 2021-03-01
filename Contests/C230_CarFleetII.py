def collideTime(car1, car2):
    if car2[1] >= car1[1]:
        return float("inf")
    else:
        return (car2[0] - car1[0]) / (car1[1] - car2[1])


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        """
        Solu 1: (O(n^2), TLE)
        From last car to first
        calc cur car's collide time with all seen cars to get min times

        Solu 2:
        """
        res = []
        for i in range(len(cars) - 1, -1, -1):
            minTime = float("inf")
            for j in range(i + 1, len(cars)):
                curTime = collideTime(cars[i], cars[j])
                minTime = min(minTime, curTime)
            if minTime == float("inf"):
                res.append(-1)
            else:
                res.append(minTime)
        return res[::-1]