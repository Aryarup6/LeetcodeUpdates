class Solution(object):
    def clearDigits(self, s):
        s=list(s)      
        x=list(s) 
        for i in x:
            if i.isnumeric():
                ind=s.index(i)
                s.pop(ind-1)
                s.remove(i)
        return "".join(s)

