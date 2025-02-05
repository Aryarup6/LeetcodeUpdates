class Solution:
    def areAlmostEqual(self, s: str, t: str) -> bool:
        return sum(map(ne,s,t))<3 and Counter(s)==Counter(t)