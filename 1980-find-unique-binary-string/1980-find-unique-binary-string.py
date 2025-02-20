
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums)
        curr=""
        return self.Generate_BinaryStrings(curr,nums,n)
    def Generate_BinaryStrings(self,curr,nums,n):
        if len(curr)==n:
            if curr not in nums:
                return curr
            return None

        for i in ['0','1']:
            binary_string=self.Generate_BinaryStrings(curr+i,nums,n)
            if binary_string:
                return binary_string
