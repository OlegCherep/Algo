class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = {"U": [],"D": [],"L": [],"R": []}
        for i in range(len(moves)):
            m[moves[i]].append(i)
        if len(m['U']) == len(m['D']) and (len(m['R']) == len(m['L'])):
            return True
        return False