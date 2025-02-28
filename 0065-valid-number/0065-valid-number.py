class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if s == "inf" or s == "-inf" or s == "+inf" or s =="Infinity" or s == "infinity" or s=="+Infinity" or s                 == "-Infinity" or s == "+infinity" or s == "-infinity" or s == "nan":
                return False
            num = float(s)
            return True
        except:
            return False