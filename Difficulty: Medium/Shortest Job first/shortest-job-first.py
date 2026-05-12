class Solution:
    def solve(self, bt):
        bt = sorted(bt)
        ct = []
        
        ct.append(bt[0])
        
        for i in range(1, len(bt)):
            ct.append(ct[-1] + bt[i])
        
        for j in range(len(ct)):
            ct[j] = ct[j] - bt[j]
        
        summ = 0    
        for k in range(len(ct)):
            summ += ct[k]
        
        return summ // len(bt)