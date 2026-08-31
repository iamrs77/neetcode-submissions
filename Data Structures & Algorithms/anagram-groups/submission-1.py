class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicti = defaultdict(list)

        for s in strs:
            sorteds = "".join(sorted(s))
            dicti[sorteds].append(s)
        
        return list(dicti.values())