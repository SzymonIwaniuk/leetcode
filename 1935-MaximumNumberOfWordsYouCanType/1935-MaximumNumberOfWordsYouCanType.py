class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_letters = set(letter for letter in brokenLetters)
        list_of_strings = text.split()
        number_of_strings = len(list_of_strings)
        broken_strings = 0

        for string in list_of_strings:
            flag = False
            for letter in string:
                if letter in broken_letters:
                    flag = True
                    break
            
            if flag:
                broken_strings += 1

        return number_of_strings - broken_strings