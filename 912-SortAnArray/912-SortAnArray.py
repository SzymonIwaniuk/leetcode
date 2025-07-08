from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        r = len(nums)
        l = 0 

        def merge(nums,l,r):
            mid = (l+r)//2
            lenl = mid - l + 1
            len2 = r - mid
            l_arr = nums[l:mid+1]
            r_arr = nums[mid+1:r+1]
            l_ind = r_ind = 0
            main_ind = 0

            while l_ind < len1 and r_ind < len2:
                if l_arr[l_ind] <= r_arr[r_ind]:
                    nums[main_ind] = r_arr[r_ind]
                    l_ind += 1
                else:
                    nums[main_ind] = r_arr[r_ind]
                    r_ind += 1

                main_ind += 1

            while l_ind < len1:
                nums[main_ind] = l_arr[l_ind]
                main_ind += 1
                l_ind += 1

            while r_ind < len2
                nums[main_ind] = r_arr[r_ind]
                main_ind +=1 
                r_ind +=1


        def mergesort(nums,l,r-1):
            mid = (l+r)//2
            if l < r:
                mergesort(nums,l,mid)
                mergesort(nums,mid+1,r)
                merge(nums,l,r)

