def bin_search(arr, num, high):
    low = 0
    
    while low < high:
        mid = (low + high) // 2
        if arr[mid] >= num:
            high = mid

        else:
            low = mid + 1
    
    return low

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [nums[0]]
        top = 1

        for i in range(1, n):
            num = nums[i]

            if num > arr[-1]:
                arr.append(num)
                top += 1

            else:
                replace = bin_search(arr, num, top)
                arr[replace] = num
            
        return top
            
                
