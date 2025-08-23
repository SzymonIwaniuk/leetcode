class MaxIntervalTree:
    left = staticmethod(lambda i: 2*i)
    right = staticmethod(lambda i: 2*i + 1)
    parent = staticmethod(lambda i: i // 2)

    def __init__(self, n):
        self.leaves = 1
        while self.leaves < n:
            self.leaves *= 2
        self.tree = [0] * 2 * self.leaves
        self.lazy = [0] * 2 * self.leaves

    def update(self, l, r, h):
        self.__update(1, 0, self.leaves - 1, l, r, h)

    def __update(self, k, klo, khi, l, r, h):
        if khi < l or klo > r:
            return

        if l <= klo and khi <= r:
            self.tree[k] = max(self.tree[k], h)
            self.lazy[k] = max(self.lazy[k], h)
            return

        self.__push(k)

        mid = (klo + khi) // 2

        self.__update(self.left(k), klo, mid, l, r, h)
        self.__update(self.right(k), mid+1, khi, l, r, h)
        self.tree[k] = max(self.tree[self.left(k)], self.tree[self.right(k)])

    def query(self, i):
        return self.__query(1, 0, self.leaves - 1, i)

    def __query(self, k, klo, khi, i):
        if klo == khi:
            return self.tree[k]
            
        self.__push(k)
        mid = (klo + khi) // 2

        if i <= mid:
            return self.__query(self.left(k), klo, mid, i)
        else:
            return self.__query(self.right(k), mid+1, khi, i)

    def __push(self, k):
        self.tree[self.left(k)] = max(self.tree[self.left(k)], self.lazy[k])
        self.lazy[self.left(k)] = max(self.lazy[self.left(k)], self.lazy[k])
        self.tree[self.right(k)] = max(self.tree[self.right(k)], self.lazy[k])
        self.lazy[self.right(k)] = max(self.lazy[self.right(k)], self.lazy[k])
        self.lazy[k] = 0


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = set()

        for l, r, h in buildings:
            points.add(l)
            points.add(r)

        sorted_points = sorted(points)
        index = {x:i for i,x in enumerate(sorted_points)}

        n = len(sorted_points)

        tree = MaxIntervalTree(n)
        for l, r, h in buildings:
            tree.update(index[l], index[r]-1, h)
        
        res = []
        prev_h = 0

        for i, x in enumerate(sorted_points):
            h = tree.query(i)
            if h != prev_h:
                res.append([x, h])
                prev_h = h

        return res
