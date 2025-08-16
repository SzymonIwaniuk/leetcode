from collections import deque


def build_map(arr, n):
    mapping = {}

    for i in range(n):
        if arr[i] not in mapping:
            mapping[arr[i]] = set()

        mapping[arr[i]].add(i)

    return mapping


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        mapping = build_map(arr, n)

        # bfs
        queue = deque()
        queue.append(0)
        times = [None] * n
        times[0] = 0
        visited = [False] * n
        visited[0] = True

        while queue:
            v = queue.popleft()

            if arr[v] in mapping:
                con = mapping[arr[v]]
                
                for u in con:
                    if not visited[u]:
                        visited[u] = True
                        queue.append(u)
                        times[u] = times[v] + 1

                del mapping[arr[v]]
                
            for i in range(v - 1, v + 2):
                if i >= 0 and i < n and not visited[i] and i != v:
                    visited[i] = True
                    queue.append(i)
                    times[i] = times[v] + 1


        return times[-1]
