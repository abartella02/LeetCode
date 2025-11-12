class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if not any(citations):
            return 0

        candidate = 0
        for i, c in enumerate(citations):
            count = 0
            num_cit = i + 1
            for cc in citations:
                if cc >= num_cit:
                    count += 1
            if count >= num_cit and num_cit > candidate:
                candidate = num_cit


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        if not any(citations):
            return 0
        num_articles = len(citations)
        citations.sort()
        for i, el in enumerate(citations):
            if num_articles - i <= el:
                # if remaining number of articles (with greater or equal amount of citations as el) is
                # less than or equal to the value of el
                return num_articles - i

        return 0


sol = Solution()
citations = [1, 3, 1]
print(sol.hIndex(citations))

"""[0, 1, 3, 5, 6]
0:
if 5 - 0 <= 0:
    false
1
if 4 - 1 <= 1:
    false

2
if 3 - 2 <= 3:
    true

3
if 5 - 1 <= 4:
    true
    
[1,3,1]
1
if 3 - 1 <= 1:
    false
1
if 2 - 1 <= 1:
    true
"""
