class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(a):
            return (a[0] ** 2 + a[1] ** 2) ** 5
        
        points.sort(key = lambda x: dist(x))
        return points[:k]