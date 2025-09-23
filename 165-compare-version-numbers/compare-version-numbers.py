class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split1 = version1.split(".")
        split2 = version2.split(".")
        p1, p2 = 0, 0

        maxLen = max(len(split1), len(split2))
        if len(split1) < len(split2):
            split1.extend([0] * (maxLen - len(split1)))
        if len(split2) < len(split1):
            split2.extend([0] * (maxLen - len(split2)))

        while p1 < len(split1) and p2 < len(split2):
            if int(split1[p1]) > int(split2[p2]):
                return 1
            if int(split1[p1]) < int(split2[p2]):
                return -1
            p1 += 1
            p2 += 1
        
        return 0