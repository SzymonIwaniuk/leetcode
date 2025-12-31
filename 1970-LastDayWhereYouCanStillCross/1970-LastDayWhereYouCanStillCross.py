def union(a, b, sets):
    rep_a = find(a, sets)
    rep_b = find(b, sets)

    _, l1, r1 = sets[rep_a]
    _, l2, r2 = sets[rep_b]

    sets[rep_a][0] = rep_b
    sets[rep_b][1] = min(l1 ,l2)
    sets[rep_b][2] = max(r1, r2)

    return rep_b


def find(a, sets):
    if sets[a][0] != a:
        return find(sets[a][0], sets)
    return a


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        # union find
        # for new water cell merge all neightbours which are water
        # hold max left and max right of set
        # so if left == 0 and right == col - 1 return days 
        sets = {}
        check = [
            (-1, -1), (-1, 0), (0 , -1), (1, -1), (-1, 1), (1, 0), (0, 1),  (1, 1)
            ]
        days = -1
        for c in cells:
            days += 1
            x = c[0] - 1
            y = c[1] - 1
            sets[(x, y)] = [(x, y), y, y]

            for n1, n2 in check:
                if (x + n1, y + n2) in sets:
                    rep = union((x, y), (x + n1, y + n2), sets)
                    _, l, r = sets[rep]
                    if l == 0 and r == col - 1:
                        return days
