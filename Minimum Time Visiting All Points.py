class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sum = 0
        for i in range(1, len(points)):
            [x1, y1] = points[i]
            [x2, y2] = points[i-1]
            x = abs(x2 -x1) 
            y = abs(y2-y1)
            sum += max(x, y)
        return sum