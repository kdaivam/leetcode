class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        return [B.index(i) for i in A]