class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        answer = set()
        prevs = set()

        for num in arr:
            curr = {num}

            for prev in prevs:
                curr.add(num | prev)
            
            answer.update(curr)
            prevs = curr
        
        return len(answer)
