class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        # edges = [[0, 1], [0, 2], [1, 3], [1, 4]]
        """ 
            adj = {
                0 : [1, 2],
                1 : [0, 3, 4]:
                2: [],
                3: [1],
                4: [1]
        }
        """
        # visited = {0, 1, 4 }

        def dfs(node, parent): # 0, -1 | 1, 0 | 4 , 1 |
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if nei in visited:
                    return False
                
                if not dfs(nei, node):
                    return False
                
            return True
            
        if not dfs(0, -1):
            return False
        
        return len(visited) == n