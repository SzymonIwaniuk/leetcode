class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        top = 1 
        n = len(s)
        score = 0

        for i in range(n):
            if s[i] == ')':
                stack.pop()
                top -= 1

                if top == 0:
                    stack.append(i)
                    top += 1
                
                else:
                    score = max(score, i - stack[-1])

            else:
                stack.append(i)
                top += 1
          
        return score

