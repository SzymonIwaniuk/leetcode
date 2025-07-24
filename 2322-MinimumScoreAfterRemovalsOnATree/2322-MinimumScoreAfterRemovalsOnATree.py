def dfs(graph: List[List[int]], 
    e1: int,
    e2: int,
    n: int,
    nums: List[int],
    ) ->  int:
    
    visited = [False for i in range(n)]

    maxi = -1
    mini = 10e10

    def dfs_visit(v: int) -> None:
        for u in graph[v]:
            # print((u ,v), e1)
            if [u, v] != e1 and [v, u] != e1 and [u, v] != e2 and [v, u] != e2:
                if visited[u] is False:
                    visited[u] = True
                    dfs_visit(u)

    
    for v in range(n):
        if visited[v] is False:
            visited[v] = True
            dfs_visit(v)
        
        # print(visited)
        cur_xor = 0
        flag = False
        for i in range(n):
            if visited[i] == True:
                flag = True
                cur_xor = cur_xor ^ nums[i]
                visited[i] = None
        
        if flag:
            maxi = max(maxi, cur_xor)
            mini = min(mini, cur_xor)
        # print(maxi, mini)

    return maxi - mini 
            

def build_graph(edges: List[List[int]], n: int) -> List[List[int]]:
    graph = [[] for v in range(n)]

    for v, u in edges:
        graph[v].append(u)
        graph[u].append(v)

    return graph


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        m = len(edges)
        n = len(nums)

        graph = build_graph(edges, n)
        res = 10e10

        for i in range(m):
            for j in range(i + 1, m):
                e1 = edges[i]
                e2 = edges[j]
                res = min(res, dfs(graph, e1, e2, n, nums))

        return res
