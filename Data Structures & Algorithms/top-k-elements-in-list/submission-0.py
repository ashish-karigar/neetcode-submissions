class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        freq = [[] for i in range(len(nums)+1)]

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        for n, c in hash_map.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        