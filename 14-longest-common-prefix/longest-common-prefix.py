class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        mn_l = min(len(s) for s in strs)

        for i in range(mn_l):
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:mn_l]