class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        all_even = all_odd = even_odd = odd_even = 0
        last_even_odd = 1
        last_odd_even = 0

        if nums[0] % 2 == 0:
            all_even = 1
            even_odd = 1
            last_even_odd = 0

        else:
            all_odd = 1
            odd_even = 1
            last_odd_even = 1

        for n in nums[1:]:
            if n % 2 == 0:
                all_even += 1
                if last_even_odd == 1:
                    even_odd += 1
                    last_even_odd = 0
                if last_odd_even == 1:
                    odd_even += 1
                    last_odd_even = 0

            else:
                all_odd += 1
                if last_even_odd == 0:
                    even_odd += 1
                    last_even_odd = 1
                if last_odd_even == 0:
                    odd_even += 1
                    last_odd_even = 1

        return max(all_even, all_odd, even_odd, odd_even)
