class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        si, pi = len(s) - 1, len(p) - 1
        
        star, last = -1, -1

        while si >= 0:
            
            if pi >= 0 and (p[pi] == s[si] or p[pi] == '?'):
                si -= 1
                pi -= 1
            
            elif pi >= 0 and p[pi] == '*':
                star = pi
                last = si
                pi -= 1
            
            elif star != -1: 
                pi = star - 1
                last -= 1
                si = last
            else:
                
                return False

        while pi >= 0 and p[pi] == '*':
            pi -= 1

        return pi < 0