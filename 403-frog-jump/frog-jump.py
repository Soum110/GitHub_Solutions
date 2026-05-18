class Solution:
    def canCross(self, stones: List[int]) -> bool:

        stone_to_index = {stone: i for i, stone in enumerate(stones)}
        dp = {}

        def f(k, ind):

            if k <= 0:
                return False

            if ind == len(stones) - 1:
                return True

            if (ind, k) in dp:
                return dp[(ind, k)]

            next_pos = stones[ind] + k

            if next_pos not in stone_to_index:
                dp[(ind, k)] = False
                return False

            nxt_ind = stone_to_index[next_pos]

            dp[(ind, k)] = (
                f(k - 1, nxt_ind) or
                f(k, nxt_ind) or
                f(k + 1, nxt_ind)
            )

            return dp[(ind, k)]

        return f(1, 0)