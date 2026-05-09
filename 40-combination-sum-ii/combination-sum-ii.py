class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates = sorted(candidates)
        def f(ind, arr, summ):
            if summ == target:
                res.append(arr[:])
                return
            if ind >= len(candidates) or summ > target:
                return

            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target - summ:
                    break

                arr.append(candidates[i])
                summ += candidates[i]
                f(i + 1, arr, summ)
                summ -= arr.pop()
        f(0, [], 0)
        return res

