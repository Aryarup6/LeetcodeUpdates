class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        
        @cache
        def backtrack(avail_chars):
            used = set()
            seqs = 0 

            for i, char in enumerate(avail_chars):
                if char in used: continue
                used.add(char)

                
                seqs += 1 + backtrack(avail_chars[:i] + avail_chars[i + 1:])
            
            return seqs

        return backtrack(tiles)