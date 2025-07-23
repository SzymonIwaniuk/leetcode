class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # top-down approach
        # memo = {}
        # n = len(s)

        # def rec(i):
        #     #print(i)
        #     if i > n - 1:
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     max_score = 0
       
        #     if i + 1 < n and s[i] == 'a' and s[i + 1] == 'b':
        #         max_score = max(max_score, rec(i + 2) + x)
            
        #     elif i + 1 < n and s[i] == 'b' and s[i + 1] == 'a':
        #         max_score = max(max_score, rec(i + 2) + y)

        #     max_score = max(max_score, rec(i + 1))

        #     memo[i] =  max_score
        #     return max_score

        # return rec(0)

        # Wrong :(

        # stack greddy approach
       
        def remove_pairs(pair, val):
            nonlocal s
            score = 0
            stack = ['dummy']
             
            for ch in s:
                if ch == pair[1] and stack[-1] == pair[0]:
                    stack.pop()
                    score += val
                else:
                    stack.append(ch)

            s = ''.join(stack[1:])
            return score 

        # Step 1 remove all occurances the one that gives us a higher score
        score = 0
        pair = 'ab' if x > y else 'ba'

        score += remove_pairs(pair, max(x, y))

        # Step 2 remove all occurances of opperation with lower score left in reduced string
        score += remove_pairs(pair[::-1], min(x, y))

        return score

        # Complexity O(n)
