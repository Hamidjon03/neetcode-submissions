class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] == x:
                return x
            return find(parent[x])
        
        def union(x, y):
            x = find(x)
            y = find(y)

            parent[y] = x

        for u, v in edges:
            if find(u) == find(v):
                return False
            union(u, v)

        roots = [i for i in range(n) if parent[i] == i]

        return len(roots) == 1