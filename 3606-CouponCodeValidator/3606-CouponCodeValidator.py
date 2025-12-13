class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        valid = []
        categories = set(["electronics", "grocery", "pharmacy", "restaurant"])

        for i in range(n):
            if code[i].replace("_", "a").isalnum() and businessLine[i] in categories and isActive[i]:
                valid.append([businessLine[i], code[i]])

        valid.sort(key = lambda x: (x[0], x[1]))
        return [code for _, code in valid]
        
        
