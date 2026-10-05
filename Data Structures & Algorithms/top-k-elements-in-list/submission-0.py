import itertools
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for x in nums:
            if x in d:
                d[x] +=1
            else:
                d[x] = 1
        
        sorted_dict_desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        

        for val in itertools.islice(sorted_dict_desc.keys(), k):
            res.append(val)
        return res