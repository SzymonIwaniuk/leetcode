def calc(formula):
    stack = []

    for ch in formula:
        if stack and stack[-1] == '*':
            stack.pop()
            num = int(stack.pop())
            num *= int(ch)
            stack.append(str(num)) 

        elif ch == '+':
            continue
        else:
            stack.append(ch)
    
    result = sum(list(map(int, stack)))
    return result


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        m = len(s)
        possibilites = set()

        correct = calc(s)

        def rec(i, stack):
            if i == m:
                result = calc(stack)
                possibilites.add(result)
                return

            new_stack = stack.copy()
            new_stack.append(s[i])
            rec(i + 1, new_stack)

            if stack and stack[-1] == '+':
                stack.pop()
                num = int(stack.pop())
                num += int(s[i])
                stack.append(str(num)) 
                rec(i + 1, stack)

            elif stack and stack[-1] == '*':
                stack.pop()
                num = int(stack.pop())
                num *= int(s[i])
                stack.append(str(num))
                rec(i + 1, stack)
        
        rec(0, [])
        possibilites.remove(correct)

        result = 0
        for answer in answers:
            if answer == correct:
                result += 5
            elif answer in possibilites:
                result += 2
        
        return result 
