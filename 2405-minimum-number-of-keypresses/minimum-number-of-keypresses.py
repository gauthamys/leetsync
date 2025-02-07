class Solution:
    def minimumKeypresses(self, s: str) -> int:
        lookup = defaultdict(int)
        ans = 0
        cnt = 0
        for c in s:
            lookup[c] += 1
        
        for i, v in enumerate(sorted(lookup.values(), reverse=True)):
            ans += ((i + 9) // 9) * v
            
        return ans