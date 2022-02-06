class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".",
                "..-.","--.","....","..",".---",
                "-.-",".-..","--","-.","---",
                ".--.","--.-",".-.","...","-","..-",
                "...-",".--","-..-","-.--","--.."] 
        lst = []
        for i in range(len(words)):
            str = ""
            for j in range(len(words[i])):
                str += morse[ord(words[i][j]) - 97]
            lst.append(str)
        
        return len(set(lst))