class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        m = {chr(97 + i) : i for i in range(26)}
        morse = [".-","-...","-.-.","-..",".",
                "..-.","--.","....","..",".---",
                "-.-",".-..","--","-.","---",
                ".--.","--.-",".-.","...","-","..-",
                "...-",".--","-..-","-.--","--.."] 
        lst = []
        for i in range(len(words)):
            str = ""
            for j in range(len(words[i])):
                str += mors[m[words[i][j]]]
            lst.append(str)
        
        return len(set(lst))