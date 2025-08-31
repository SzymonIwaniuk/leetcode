class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        i = 0
        MOD = 10**9 + 7

        n_copy = n

        while n_copy:
            b = n_copy % 2
            if b == 1:
                powers.append(2**i) 
        
            n_copy //= 2
            i += 1

        m = len(powers)
        prefix = [0 for _ in range(m)]
        prefix[0] = powers[0]

        for i in range(1, m):
            prefix[i] = powers[i] * prefix[i-1]
        
        out = []

        for l, r in queries:
            out.append((prefix[r] // (prefix[l-1] if l > 0 else 1)) % MOD)

        return out
