class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        first_max = defaultdict(lambda: -maxsize)
        second_max = defaultdict(lambda: -maxsize)

        for num in nums:
            digits_sum = sum(map(int, str(num)))

            if num > first_max[digits_sum]:
                second_max[digits_sum] = first_max[digits_sum]
                first_max[digits_sum] = num

            elif num > second_max[digits_sum]:
                second_max[digits_sum] = num

        max_sum = -1

        for digits_sum in second_max.keys():
            max_sum = max(max_sum, first_max[digits_sum] + second_max[digits_sum])

        if max_sum == -maxsize:
            return -1

        return max_sum