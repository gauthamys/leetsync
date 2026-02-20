class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        ar = []
        for part in s:
            if part == '.' or part == '':
                continue
            if part == '..':
                if ar: ar.pop()
                continue
            ar.append(part)
        return '/' + '/'.join(ar)
            
            