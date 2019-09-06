class Solution:
    def largestUniqueNumber(self, a: List[int]) -> int:
        x = list(filter(lambda i: a.count(i) == 1, a))
        return max(x) if len(x)>0 else -1