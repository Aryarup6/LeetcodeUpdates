class Solution:
    def removeOccurrences(self, string: str, part: str) -> str:
        while part in string:
            string = string.replace(part, '', 1)
        return string