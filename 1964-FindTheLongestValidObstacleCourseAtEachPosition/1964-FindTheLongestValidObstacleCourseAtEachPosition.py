def bin_search_right(seq, obstacle, high):
    low = 0

    while low < high:
        mid = (low + high) // 2

        if seq[mid] > obstacle:
            high = mid

        else:
            low = mid + 1
    
    return low


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        seq = [obstacles[0]]
        top = 1
        res = [1] * n

        for i in range(1, n):
            obstacle = obstacles[i]

            if obstacle >= seq[-1]:
                seq.append(obstacle)
                top += 1
                res[i] = top

            else:
                replace = bin_search_right(seq, obstacle, top)
                seq[replace] = obstacle
                res[i] = replace + 1

        return res
