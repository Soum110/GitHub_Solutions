class Solution:
    def romanToInt(self, s: str) -> int:
        l = list(s)
        dic = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        num = 0
        i = 0
        while i < len(l):
            if i + 1 < len(l) and dic[l[i+1]] > dic[l[i]]:
                num = num + (dic[l[i+1]] - dic[l[i]])
                i += 2
            else:
                num = num + dic[l[i]]
                i+=1
        return num