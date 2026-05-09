class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def f(ind, arr, summ):
            if summ == target:
                res.append(arr[:])
                return
            if ind >= len(candidates) or summ > target:
                return
            #Take it
            arr.append(candidates[ind])
            summ += candidates[ind]
            f(ind, arr, summ)

            #Not Take
            summ -= arr.pop()
            f(ind + 1, arr, summ)
        f(0, [], 0)
        return res
        
