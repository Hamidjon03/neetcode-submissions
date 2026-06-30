class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for p in points:
            x = p[0]
            y = p[1]

            dist = x**2 + y**2
            distances.append([dist, p])

        distances.sort()

        result = []

        for i in range(k):
            result.append(distances[i][1])

        return result