class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        count, i = 0, 0
        for j in range(i, len(s)):
            if s[j] in dic and dic[s[j]] >= i:
                i = dic[s[j]] + 1

            dic[s[j]] = j
            count = max(count, j - i + 1)
        return count

# TC = O(n)
# SC = O(n) 