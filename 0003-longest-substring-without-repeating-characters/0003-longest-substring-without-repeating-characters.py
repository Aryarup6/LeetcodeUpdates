class Solution:
    def lengthOfLongestSubstring(self, s):
        st = maxL = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and st <= usedChar[s[i]]:
                st = usedChar[s[i]] + 1
            else:
                maxL = max(maxL, i - st + 1)

            usedChar[s[i]] = i

        return maxL