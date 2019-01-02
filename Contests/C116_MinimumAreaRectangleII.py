'''

Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.



Example 1:



Input: [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:



Input: [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:



Input: [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
Example 4:



Input: [[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [2,1],[2,3],[3,3],[3,1], with an area of 2.


Note:

1 <= points.length <= 50
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
Answers within 10^-5 of the actual value will be accepted as correct.
'''


class Solution(object):
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        def is_vec_vetical(vec1, vec2):
            return (vec1[0] * vec2[0] + vec1[1] * vec2[1]) == 0

        def get_vec(pt1, pt2):
            return [pt1[0] - pt2[0], pt1[1] - pt2[1]]

        def get_area(vec1, vec2):
            return (vec1[0] ** 2 + vec1[1] ** 2) ** 0.5 * (vec2[0] ** 2 + vec2[1] ** 2) ** 0.5

        def calc_area_ordered(pts):
            vec0 = get_vec(pts[0], pts[1])
            vec1 = get_vec(pts[1], pts[2])
            vec2 = get_vec(pts[2], pts[3])
            vec3 = get_vec(pts[3], pts[0])

            if is_vec_vetical(vec1, vec2) and is_vec_vetical(vec2, vec3) and is_vec_vetical(vec3,
                                                                                            vec0) and is_vec_vetical(
                    vec0, vec1):
                return get_area(vec0, vec1)
            else:
                return 0

        def calc_area_general(pts):
            return calc_area_ordered(pts) or calc_area_ordered([pts[0], pts[1], pts[3], pts[2]]) or calc_area_ordered(
                [pts[0], pts[2], pts[1], pts[3]])

        '''
        Brutal force
        '''
        num_pts = len(points)
        min_area = 0
        for i in range(num_pts):
            for j in range(i + 1, num_pts):
                for k in range(j + 1, num_pts):
                    for l in range(k + 1, num_pts):
                        cur_area = calc_area_general([points[i], points[j], points[k], points[l]])
                        if cur_area != 0:
                            if min_area == 0:
                                min_area = cur_area
                            else:
                                min_area = min(min_area, cur_area)
        return min_area            