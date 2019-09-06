class Solution:
    def removeVowels(self, s: str) -> str:
        return "".join(list( filter(lambda x: x not in "aeiou", s)))