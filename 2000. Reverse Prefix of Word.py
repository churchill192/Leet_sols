class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch in word:
            rev = word[:word.index(ch)+1]
            s = rev[::-1]
            rem = word[word.index(ch)+1:]
            return s+rem
        else:
            return word
        

        