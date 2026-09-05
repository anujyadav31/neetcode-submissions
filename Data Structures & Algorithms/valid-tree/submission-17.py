class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = {i:[] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n

######## find-union solution ########
'''
        if len(edges) > n - 1: # find-union can work without this
            return False       # find-union can work without this
        par = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges:
            #res -= union(n1, n2)
            if not union(n1, n2):
                return False
            res -= 1
        #return res
        return res == 1
'''
        