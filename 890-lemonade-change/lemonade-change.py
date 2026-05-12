class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        mapp = {5 : 0, 10 : 0, 20 : 0}
        i = 0
        while i < len(bills):
            if bills[i] == 5:
                if bills[i] in mapp:
                    mapp[bills[i]] += 1
                else:
                    mapp[bills[i]] = 1
            elif bills[i] == 10:
                if mapp[5] <= 0:
                    return False
                mapp[5] -= 1

                if bills[i] in mapp:
                    mapp[bills[i]] += 1
                else:
                    mapp[bills[i]] = 1

            elif bills[i] == 20:
                if mapp[10] <= 0:
                    if mapp[5] >= 3:
                        mapp[5] -= 3
                    else:
                        return False
                elif mapp[10] > 0 and mapp[5] > 0:
                    mapp[10] -= 1
                    mapp[5] -= 1
                else:
                    return False
                if bills[i] in mapp:
                    mapp[bills[i]] += 1
                else:
                    mapp[bills[i]] = 1
            i += 1
                    
        return True


