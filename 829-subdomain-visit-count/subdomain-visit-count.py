class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        m = {}
        for pair in cpdomains:
            count, domain = pair.split(" ")
            count = int(count)
            subdomains = domain.split('.')
            j = len(subdomains) - 1
            while j >= 0:
                key = '.'.join(subdomains[j:]) 
                m[key] = m.get(key, 0) + count
                j -= 1
        
        return [f'{m[d]} {d}' for d in m]

