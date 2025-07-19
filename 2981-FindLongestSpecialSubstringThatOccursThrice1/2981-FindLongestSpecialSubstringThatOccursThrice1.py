class Solution:
    def maximumLength(self, s: str) -> int:
        # Brute
        n = len(s)
        res = -1

        for i in range(n):

            # Word starting index
            for j in range(i + 1, n - 1):
                # Check that substring is special, if not break and go to next iteration
                if s[i] != s[j-1]:
                    break

                # Check if the new length grater than max len
                if (j - i) > res:
                    cnt = 0
                    word = s[i:j]
                    
                    # Loop through string couting special substrings equals to current
                    for k in range(i, n - (j - i) + 1):
                        if s[k:k + (j - i)] == word:
                            cnt += 1
                    
                    # Check if we find at least three and update res
                    if cnt >= 3:
                        res = (j - i)
        return res

