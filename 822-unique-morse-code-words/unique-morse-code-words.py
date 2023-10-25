class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        if len(words) == 1:
            return 1

        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        new = []
        for word in words:
            temp = ''
            for j in word:
                temp += morse[ord(j) - ord('a')]
            new.append(temp)

        unique = []
        for i in new:
            if i not in unique:
                unique.append(i)
        return len(unique)             