class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False
        
        if self.rank[pa] < self.rank[pb]:
            self.parent[pa] = pb
        elif self.rank[pb] < self.rank[pa]:
            self.parent[pb] = pa
        else:
            self.parent[pb] = pa
            self.rank[pa] += 1
        return True


class Solution:
    def maxStability(self, n, edges, k):

        def can(S):
            dsu = DSU(n)
            upgrades = k
            count = 0

            # add mandatory edges
            for u,v,s,must in edges:
                if must == 1:
                    if s < S:
                        return False
                    if not dsu.union(u,v):
                        return False
                    count += 1

            optional = []

            for u,v,s,must in edges:
                if must == 0:
                    optional.append((u,v,s))

            # try edges without upgrade first
            for u,v,s in optional:
                if s >= S and dsu.union(u,v):
                    count += 1

            # try upgraded edges
            for u,v,s in optional:
                if count == n-1:
                    break
                if s < S and s*2 >= S and upgrades > 0:
                    if dsu.union(u,v):
                        upgrades -= 1
                        count += 1

            return count == n-1

        left, right = 0, max(s*2 for _,_,s,_ in edges)
        ans = -1

        while left <= right:
            mid = (left+right)//2
            if can(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1

        return ans