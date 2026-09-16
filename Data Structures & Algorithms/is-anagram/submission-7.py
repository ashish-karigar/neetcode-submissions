class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # ascii for a - z = 97 - 122
        counts = [0]*26

        for _ in s:
            index = ord(_) - 97
            counts[index] += 1

        for _ in t:
            index = ord(_) - 97
            counts[index] -= 1

            if counts[index]<0:
                return False

        return True


        