from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k: return 0  
        
        left, right = 1, max(candies)
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if self.canDistribute(candies, k, mid):
                result = mid
                left = mid + 1 
            else:
                right = mid - 1 
        
        return result

    def canDistribute(self, candies: List[int], k: int, val: int) -> bool:
        return sum(c // val for c in candies) >= k