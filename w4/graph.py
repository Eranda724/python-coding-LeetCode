from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        p = [-1] * n

        def bfs_check(start_node):
            q = deque([start_node])
            p[start_node] = 0

            while q:
                current = q.popleft()
                for adj in graph[current]:
                    if p[adj] == -1:
                        p[adj] = 1 - p[current]
                        q.append(adj)
                    elif p[adj] == p[current]:
                        return False
            return True

        for node in range(n):
            if p[node] == -1:
                if not bfs_check(node):
                    return False
        
        return True
