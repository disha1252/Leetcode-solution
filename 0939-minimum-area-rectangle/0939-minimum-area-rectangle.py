class Solution:
    def minAreaRect(self, points):
        point_set = set(map(tuple, points))
        n = len(points)
        min_area = float("inf")

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]

                # check diagonal points
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x2-x1) * abs(y2-y1)
                        min_area = min(min_area, area)

        return 0 if min_area == float("inf") else min_area