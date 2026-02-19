class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in m:
                m[ss].append(s)
            else:
                m[ss] = [s]
        return m.values()
