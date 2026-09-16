class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # ascii for a - z = 97 - 122
        seen = {}

        for _ in s:
            seen[_] = seen.get(_,0)+1

        for _ in t:
            if _ in seen:
                seen[_] -= 1
                if seen[_] == 0:
                    del seen[_]
            else:
                return False

        return True


        