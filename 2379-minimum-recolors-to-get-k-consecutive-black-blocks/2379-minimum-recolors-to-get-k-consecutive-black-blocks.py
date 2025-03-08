class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        c=k
        for i in range(len(blocks)-(k-1)):
            m=0
            for i in (blocks[i:i+k]):
                if i=="W":
                    m+=1
            if m<c:
                c=m
        return c