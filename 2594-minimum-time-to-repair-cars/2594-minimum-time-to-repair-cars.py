class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def isValidTime(time):
            cars_done = 0
            for rank, workers in ranks.items():
                
                cars_done += workers * floor(sqrt(time / rank)) 
            return cars_done >= cars 

        ranks = Counter(ranks) 
        
        
        left, right = 0, max(ranks) * ceil(cars / len(ranks)) ** 2
        while left < right: 
            mid = (left + right) // 2

            if isValidTime(mid):
                right = mid 
            else:
                left = mid + 1 

        return left 