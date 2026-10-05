class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary =  defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord('a') - ord(c)]+=1
            
            key = tuple(count)
            dictionary[key].append(s)
        
        return list(dictionary.values())