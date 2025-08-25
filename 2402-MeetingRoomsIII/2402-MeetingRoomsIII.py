from math import log2, ceil

def insert(current, start, end, tree, first_element, uses):
    if current >= first_element:
        uses[current - first_element] += 1
        tree[current] = max(tree[current], start) + (end - start)
        return tree[current]

    left = 2 * current + 1
    right = 2 * current + 2

    if tree[left] <= tree[right]:
        finish_time = insert(left, start, end, tree, first_element, uses)
    else:
        finish_time = insert(right, start, end, tree, first_element, uses)

    tree[current] = min(tree[left], tree[right])
    return tree[current]


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # Interval Tree
        uses = [0] * n
        p = ceil(log2(n))
        tree = [0] * (2 ** (p + 1) - 1)
        first_element = 2 ** p - 1
        meetings.sort(key=lambda meeting: meeting[1])
        print(meetings)

        for i in range(first_element + n, 2 ** (p + 1) - 1):
            tree[i] = float('inf')

        for start, end in meetings:
            insert(0, start, end, tree, first_element, uses)

        print(uses)
        return uses.index(max(uses))
