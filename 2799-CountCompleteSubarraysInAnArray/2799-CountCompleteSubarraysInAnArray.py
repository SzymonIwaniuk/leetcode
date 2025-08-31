class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        unique = set(nums)
        cnt = 0

        for i in range(n):
            curr = set()
            for j in range(i,n):
                    curr.add(nums[j])
                    if curr == unique:
                        cnt += 1

        return cnt
