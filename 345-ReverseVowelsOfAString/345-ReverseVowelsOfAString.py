class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        string = list(s)
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, n-1

        while i < j:
            if string[i] in vowels and string[j] in vowels:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1

            elif string[i] in vowels:
                j -= 1

            elif string[j] in vowels:
                i += 1

            else:
                i += 1
                j -= 1

        return "".join(string)