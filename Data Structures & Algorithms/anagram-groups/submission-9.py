class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for _str in strs:
            key = tuple(sorted(_str))
            res.setdefault(key, []).append(_str)
        return list(res.values())