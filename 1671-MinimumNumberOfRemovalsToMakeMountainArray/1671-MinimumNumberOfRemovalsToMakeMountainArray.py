def bin_search(seq, num, high):
    low = 0
    
    while low < high:
        mid = (low + high) // 2
        if seq[mid] >= num:
            high = mid

        else:
            low = mid + 1
    
    return low


def lis(array: List[int], n) -> int:
    longest = [1] * n

    seq = [array[0]]
    top = 1

    for i in range(1, n):
        num = array[i]

        if num > seq[-1]:
            seq.append(num)
            top += 1

        else:
            replace = bin_search(seq, num, top)
            seq[replace] = num
        
        longest[i] = top

    return longest

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Longest increasing subsequence inclusive to i-th element
        LIS = lis(nums, n)

        # Also lis but in reversed array so longest decreasing subsequence to i-th element
        LDS = lis(nums[::-1], n)[::-1]

        # length of widest mountain
        l = 0
        
        for i in range(n):
            if LIS[i] > 1 and LDS[i] > 1:
                l = max(l, LIS[i] + LDS[i] - 1)

        # Number of removed elements equals len of whole array - len of mountain
        return n - l
        
