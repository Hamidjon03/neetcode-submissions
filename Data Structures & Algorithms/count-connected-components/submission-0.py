class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
            union(u, v)

        roots = [i for i in range(n) if parent[i] == i]

        return len(roots)
