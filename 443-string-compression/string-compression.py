class Solution:
    def compress(self, chars: List[str]) -> int:
        cur = ''
        i = 0
        s = ''
        count = 0
        while i < len(chars):
            if chars[i] == cur:
                while i < len(chars) and chars[i] == cur:
                    count += 1
                    chars.pop(i)                 
            else:
                print(cur, count)
                if count > 1:
                    if count >= 10:
                        for j in str(count):
                            chars.insert(i, j)
                            i += 1
                    else:
                        chars.insert(i, str(count))
                        i += 1

                s += cur
                s += str(count)
                cur = chars[i]
                count = 1
                i += 1

        if count > 1:
            s += str(count)
            if count >= 10:
                for j in str(count):
                    chars.append(j)
            else:
                chars.append(str(count))

        return len(s)
            