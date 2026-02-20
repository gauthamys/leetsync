class Solution:
    def simplifyPath(self, path: str) -> str:
        l = 0
        ar = []
        while l < len(path):
            if path[l] == '.':
                l += 1
                if l < len(path) and path[l] == '.':
                    l += 1
                    if l < len(path) and path[l] != '/':
                        cur = '..' + path[l]
                        l += 1
                        while l < len(path) and path[l] != '/':
                            cur += path[l]
                            l += 1
                        ar.append(cur)
                    else:
                        if ar: ar.pop()
                elif l < len(path) and path[l] != '/':
                    cur = '.' + path[l]
                    l += 1
                    while l < len(path) and path[l] != '/':
                        cur += path[l]
                        l += 1
                    ar.append(cur)
            elif path[l] == '/':
                l += 1
                while l < len(path) and path[l] == path[l - 1]:
                    l += 1
                continue
            else:
                cur = ''
                while l < len(path) and path[l] != '/':
                    cur += path[l] 
                    l += 1
                ar.append(cur)
                l += 1
        return '/' + '/'.join(ar)