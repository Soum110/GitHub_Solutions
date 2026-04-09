class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in range(len(strs)):
            key = str(sorted(strs[i]))
            if key not in dic:
                dic[key] = []
            dic[key].append(strs[i])
        res = []
        for i, v in dic.items():
            res.append(v)
        return res
            