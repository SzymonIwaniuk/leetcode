class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        counter = {}
        for ch in s:
            if ch not in counter:
                counter[ch] = 1

            else:
                counter[ch] += 1
        
        available = set()
        for ch, cnt in counter.items():
            if cnt >= k:
                available.add(ch)

        @cache 
        def rec(i, string):
            if i == n:
                m = len(string)
                if m % k != 0:
                    return ""
                else:
                    # print(string)
                    segment_len = m // k
                    segment = string[:segment_len]
                    if segment * k == string:
                        return segment
                    else:
                        return ""

            out_string = ""

            if s[i] in available:
                out_string = max(
                    rec(i + 1, string + s[i]), 
                    rec(i + 1, string), 
                    key=lambda x: (len(x), x)
                )

            else:
                out_string = rec(i + 1, string)
                
            return out_string
        
        return rec(0, "")
        
