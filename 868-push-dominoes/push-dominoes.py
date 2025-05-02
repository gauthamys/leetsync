class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        q = []
        copy = [None] * len(dominoes)
        for i in range(len(dominoes)):
            if dominoes[i] != '.':
                copy[i] = 1 if dominoes[i] == 'R' else -1
                q.append((i, dominoes[i]))

        while q:
            qLen = len(q)
            children = defaultdict(int)
            for _ in range(qLen):
                pos, direction = q.pop(0)
                if direction == 'R' and pos + 1 < len(dominoes) and copy[pos + 1] is None:
                    child = pos + 1
                    children[child] += 1
                if direction == 'L' and pos - 1 >= 0 and copy[pos - 1] is None:
                    child = pos - 1
                    children[child] -= 1

            for child in children:
                copy[child] = children[child]
                if children[child] != 0:
                    q.append((child, 'L' if copy[child] == -1 else 'R'))

        res = ''
        for c in copy:
            if c == -1:
                res += 'L'
            elif c == 1:
                res += 'R'
            else:
                res += '.'
        return res

            