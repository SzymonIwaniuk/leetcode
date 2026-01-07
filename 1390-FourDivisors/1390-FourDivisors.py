class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def count_factors(n):
            factors = [1, n]
            cnt = 2
            for i in range(2, int(sqrt(n) + 1)): # int much better than floor
                if n % i == 0:
                    factors.append(i)
                    cnt += 1
                    if n // i != i:
                        cnt += 1
                        factors.append(n // i)
                       
            return sum(factors) if cnt == 4 else 0

        ans = 0
        memo = {}

        for n in nums:
            if n in memo:
                ans += memo[n]
            else:
                sum_fac = count_factors(n)
                memo[n] = sum_fac
                ans += sum_fac
        
        return ans
