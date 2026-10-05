class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i  in range(len(nums) +  1)]
        res = []

        for n in nums:
            count[n] = count.get(n,0) + 1
        for c , n in count.items():
            freq[n].append(c)


        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                if len(res) != k:
                    res.append(n)

        return res 


        