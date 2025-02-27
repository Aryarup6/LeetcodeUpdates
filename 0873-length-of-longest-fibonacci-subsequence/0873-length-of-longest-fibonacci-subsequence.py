class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        fib_lens = {}
        set_arr = set(arr)

        for b, c in combinations(arr, 2):
            a = c - b
            if a < b and a in set_arr: 

                fib_lens[(b, c)] = fib_lens.get((a, b), 2) + 1
                
        return max(fib_lens.values(), default = 0)       