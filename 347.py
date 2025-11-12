from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            if hash.get(i, None):
                hash[i] += 1
            else:
                hash[i] = 1

        return [i for (i, _) in sorted(hash.items(), key=lambda x: -x[1])][:k]
