class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # O(n^2)
        n = len(nums)

        """
        subsums = [[-1 for i in range(n)] for j in range(n)]

        for i in range(n):
            unique = set()
            subsum = 0

            for j in range(i,n):
                if nums[j] in unique:
                    break

                unique.add(nums[j])
                subsum += nums[j]
                subsums[i][j] = subsum
        
        max_score = 0

        for i in range(n):
            for j in range(i,n):
                max_score = max(max_score, subsums[i][j])

        return max_score
        """


        # two pointers approach O(n)

        max_score = curr_score = 0
        i = j = 0
        unique = set()

        while j < n:
            # Moving j pointer if num is unique in subarray we can add without really thinking about it,
            # update current sum and max score
            if nums[j] not in unique:
                curr_score += nums[j]
                unique.add(nums[j])
                j += 1
                max_score = max(max_score, curr_score)

            # If not we move i pointer till we find num equlas to j removing nums in subarray
            else:
                while nums[i] != nums[j]:
                    curr_score -= nums[i]
                    # print(i,j, unique)
                    unique.remove(nums[i])
                    i += 1
                # And we want jump +1 to not take repeated num
                curr_score -= nums[i]
                unique.remove(nums[i])
                i += 1
            
        return max_score
