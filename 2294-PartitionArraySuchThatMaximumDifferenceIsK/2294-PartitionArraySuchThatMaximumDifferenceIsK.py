class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        mini = nums[0]
        result = 1

        for i in range(1, n):
            if nums[i] > mini + k:
                result += 1
                mini = nums[i]

        return result
