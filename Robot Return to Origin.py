class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = {"U": 0,"D": 0,"L": 0,"R": 0}
        for i in range(len(moves)):
            m[moves[i]] += 1
        return (m['U'] == m['D']) and (m['R'] == m['L'])
