class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = dict()
        for s in strs:
            k = [0] * 26
            for c in s:
                k[ord(c) - ord('a')] += 1
            key = tuple(k)
            if key in m.keys():
                m[key].append(s)
            else:
                m[key] = [s]
        #print(m)
        return [v for v in m.values()]
