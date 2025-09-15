class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)

        if n < 3: return False
        
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
        digits = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

        vowel = False
        consonant = False

        for ch in word:
            if ch in digits:
                continue
            elif ch.lower() in vowels:
                vowel = True
            elif ch.lower() in consonants:
                consonant = True
            else:
                return False
        
        return vowel and consonant