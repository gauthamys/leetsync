class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split('/')
        print(s)
        ar = []
        for part in s:
            if part == '.' or part == '':
                continue
            if part == '..':
                if ar: ar.pop()
            else:
                ar.append(part)
        print(ar)
        return '/' + '/'.join(ar)
            
            