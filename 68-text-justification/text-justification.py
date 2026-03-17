class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def make_sentence(cur: List[str], last=False) -> str:
            if len(cur) == 1 or last:
                s = ' '.join(cur)
                return s + ' ' * (maxWidth - len(s))

            total_letters = sum(len(word) for word in cur)
            total_spaces = maxWidth - total_letters
            gaps = len(cur) - 1

            space_each = total_spaces // gaps
            extra = total_spaces % gaps

            res = []
            for i in range(gaps):
                res.append(cur[i])
                spaces = space_each + (1 if i < extra else 0)
                res.append(' ' * spaces)
            res.append(cur[-1])

            return ''.join(res)

        res = []
        cur = []
        cur_len = 0

        for word in words:
            if cur_len + len(cur) + len(word) > maxWidth:
                res.append(make_sentence(cur))
                cur = [word]
                cur_len = len(word)
            else:
                cur.append(word)
                cur_len += len(word)

        res.append(make_sentence(cur, last=True))
        return res