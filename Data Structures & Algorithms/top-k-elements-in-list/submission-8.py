class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [ [] for i in range(len(nums)+1)]

        for n,c in count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                if len(result)!=k:
                    result.append(n)
        return result


