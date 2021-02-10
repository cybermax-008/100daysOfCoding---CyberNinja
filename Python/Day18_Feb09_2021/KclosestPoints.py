class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        dist = {}
        for ind,point in enumerate(points):
            d = sqrt(point[0]**2 + point[1]**2)
            dist[ind] = (d,point)
        dist = sorted(dist.items(),key=lambda x:x[1][0])
        
        return [dist[i][1][1] for i in range(K)]

class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        points.sort(key = lambda x: x[0]**2+x[1]**2)

        return points[:K]