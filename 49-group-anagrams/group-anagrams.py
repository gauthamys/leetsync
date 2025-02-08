class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = defaultdict(list)
        for s in strs:
            m[''.join(sorted(s))].append(s)
        
        return list(m.values())