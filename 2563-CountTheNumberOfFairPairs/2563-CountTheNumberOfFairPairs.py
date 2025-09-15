def binsearch_left(arr, num, top):
    left = 0
    right = top

    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= num:
            right = mid

        else:
            left = mid + 1
    
    return left

def binsearch_right(arr, num, top):
    left = 0
    right = top

    while left < right:
        mid = (left + right) // 2
        if arr[mid] > num:
            right = mid

        else:
            left = mid + 1
    
    return left



class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        print(nums)
        for i in range(n):

            k = binsearch_left(nums, lower - nums[i], n)
            l = binsearch_right(nums, upper - nums[i], n)
            res += l - k

        for i in range(n):
            if lower <= 2 * nums[i] <= upper:
                res -= 1

        return res // 2
        

