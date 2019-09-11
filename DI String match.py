class Solution:
    def diStringMatch(self, a: str) -> List[int]:
        low = 0 
        high = len(a)
        res = []
        for i in a:
            if i == 'I':
                res.append(low)
                low += 1
            else:
                res.append(high)
                high -= 1
                
        res += [high]   #add left out element to the result
        
        return res