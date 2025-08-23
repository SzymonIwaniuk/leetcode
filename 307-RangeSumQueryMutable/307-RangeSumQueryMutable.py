class NumArray:
    left = staticmethod(lambda i: 2*i)
    right = staticmethod(lambda i: 2*i + 1)

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.leaves = 1
        while self.leaves < self.n:
            self.leaves *= 2

        self.tree = [0] * (2 * self.leaves)

        for i in range(self.n):
            self.tree[self.leaves + i] = nums[i]

        for i in range(self.leaves-1, 0, -1):
            self.tree[i] = self.tree[self.left(i)] + self.tree[self.right(i)]

    def update(self, index: int, val: int) -> None:
        self.__update(1, 0, self.leaves-1, index, val)

    def __update(self, k, klo, khi, index, val):
        if klo == khi:
            self.tree[k] = val
            return

        mid = (klo + khi) // 2
        if index <= mid:
            self.__update(self.left(k), klo, mid, index, val)
        else:
            self.__update(self.right(k), mid+1, khi, index, val)

        self.tree[k] = self.tree[self.left(k)] + self.tree[self.right(k)]

    def sumRange(self, left: int, right: int) -> int:
        return self.__sumRange(1, 0, self.leaves-1, left, right)

    def __sumRange(self, k, klo, khi, l, r):
        if khi < l or klo > r:
            return 0

        if l <= klo and khi <= r:
            return self.tree[k]

        mid = (klo + khi) // 2
        return self.__sumRange(self.left(k), klo, mid, l, r) + \
               self.__sumRange(self.right(k), mid+1, khi, l, r)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
