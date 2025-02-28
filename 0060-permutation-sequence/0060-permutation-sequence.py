class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        temp = []
        count = {str(i):1 for i in range(1,n+1)}
        def backtrack():
            if len(res)<k:
                if len(temp)==n:
                    res.append("".join(temp))
                    return 
                for ch,v in count.items():
                    if v>0:
                        count[ch]-=1
                        temp.append(ch)
                        backtrack()
                        count[ch]+=1
                        temp.pop()
                return 
            else:
                return 
        backtrack()
        return res[k-1]      