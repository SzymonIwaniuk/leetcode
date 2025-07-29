class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # max_bits = [0] * n
        # max_bits[-1] = nums[-1]

        # # step 1 -> compute max bitwise or in subarrays B(i->n)
        # # Complexity O(n)
        # for i in range(n - 2, -1, -1):
        #     max_bits[i] = max_bits[i + 1] | nums[i]
        
        # answer = []

        # step 2 -> compute len of subarray which meets task requirements
        # Complexity O(n^2)
        # Working but to slow :) 57/59 tests 
        # for i in range(n):
        #     cur_bit = 0 

        #     for j in range(i, n):
        #         cur_bit |= nums[j]
        #         if cur_bit == max_bits[i]:
        #             answer.append(j - i + 1)
        #             break
        
        # return answer

        answer = [1] * n

        for i in range(1, n):
            x = nums[i]

            j = i - 1
            while j >= 0 and (nums[j] | x) != nums[j]:
                #print(j)
                answer[j] = i - j + 1
                nums[j] |= x
                j -= 1

        return answer 
