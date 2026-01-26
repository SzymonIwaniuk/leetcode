class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n = len(arr)
        arr.sort()
        mini = min(abs(arr[i + 1] - arr[i]) for i in range(n - 1))
        return [[arr[i], arr[i + 1]] for i in range(n - 1) if abs(arr[i + 1] - arr[i]) == mini]
