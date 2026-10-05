class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0

        for d in digits:
            res*=10
            res+=d


        res+=1
        arr = [int(digit) for digit in str(res)]
        
        return arr

        